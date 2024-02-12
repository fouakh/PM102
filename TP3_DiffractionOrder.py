import numpy as np
import matplotlib.pyplot as plt

class DiffractionOrder:
    def __init__(self, data_g_file, data_b_file, data_r_file):
        self.data_g = np.loadtxt(data_g_file)
        self.data_b = np.loadtxt(data_b_file)
        self.data_r = np.loadtxt(data_r_file)

        self.xg = self.data_g[:, 0]
        self.yg = self.data_g[:, 1]
        self.yr = self.data_r[:, 1]
        self.yb = self.data_b[:, 1]

        self.wavelength_ref = 600
        self.wavelengths = np.array([440, 540, 640])
        self.sigma = self.wavelength_ref / self.wavelengths
        self.dist_order1 = 0 * self.wavelengths

        self.a = 4
        self.N = 40
        self.lenWindow = 600
        self.d = self.lenWindow / self.N
        self.alpha = self.a * self.sigma
        self.delta = self.d * self.sigma

        self.x = np.arange(-500, 501, 1)
        self.X, self.Y = np.meshgrid(self.x, self.x)

        self.Red_Img = np.zeros_like(self.X, dtype=np.float64)
        self.Blue_Img = np.zeros_like(self.X, dtype=np.float64)
        self.Green_Img = np.zeros_like(self.X, dtype=np.float64)

    def fft_wl(self, j):
        grating = np.zeros_like(self.X)
        for i in range(-self.N // 2, self.N // 2 + 1):
            x_offset = i * self.delta[j]
            mask = (np.abs(self.X - x_offset) <= self.alpha[j] / 2) & (np.abs(self.Y) <= self.lenWindow / 2)
            grating[mask] = 1

        ft = np.fft.fftshift(grating)
        ft = np.fft.fft2(ft)
        ft = np.fft.fftshift(ft)

        index = np.unravel_index(np.argmax(self.xg == self.wavelengths[j]), self.xg.shape)

        silly_coeff = (100 * self.sigma[j] ** 2 * self.a * self.N * 1000)
        self.Red_Img += self.yr[index] / silly_coeff * np.abs(ft)
        self.Blue_Img += self.yb[index] / silly_coeff * np.abs(ft)
        self.Green_Img += self.yg[index] / silly_coeff * np.abs(ft)       

    def calculate_rgb_image(self):
        for j in range(len(self.wavelengths)):
            self.fft_wl(j)

        another_silly_coeff = 6
        self.Red_Img = 255 * self.Red_Img * another_silly_coeff
        self.Blue_Img = 255 * self.Blue_Img * another_silly_coeff 
        self.Green_Img = 255 * self.Green_Img * another_silly_coeff 

        self.Red_Img = self.Red_Img.astype(int)
        self.Blue_Img = self.Blue_Img.astype(int)
        self.Green_Img = self.Green_Img.astype(int)

        self.RGB_Image = np.stack([self.Red_Img, self.Green_Img, self.Blue_Img], axis=-1)
        self.RGB_Image = np.clip(self.RGB_Image, 0, 255) 
        
    def subplot(self, i, point1, point2):
        self.dist_order1[i] = np.linalg.norm(np.array(point2) - np.array(point1))
        plt.subplot(len(self.wavelengths)*100 + 10 + i + 1)
        if i == 0:
            plt.title("Ordre 1 de Diffraction")
        plt.imshow(self.RGB_Image)
        arrow_props = dict(facecolor='none', edgecolor='yellow', arrowstyle='<->', linestyle='dashed', lw=1)
        plt.annotate('', xy=point1, xytext=point2, arrowprops=arrow_props, fontsize=8, ha='center', va='center')
        plt.text((point1[0] + point2[0]) / 2, (point1[1] + point2[1]) / 2 - 6, 
                f'Distance: {self.dist_order1[i]:.2f} p',color='yellow', ha='center', va='center', fontsize=8)
        plt.xlim([420, 590])
        plt.ylim([485, 515])

    def plot_all(self):
        points1 = [(451, 500) , (440, 500), (429, 500)]
        points2 = [(500, 500) , (500, 500), (500, 500)]
        for i in range(len(self.wavelengths)):
            self.subplot(i, points1[i], points2[i])
        plt.show()

if __name__ == '__main__':
    diffraction_order = DiffractionOrder('Green-KAF-8300.dat', 'Blue-KAF-8300.dat', 'Red-KAF-8300.dat')
    diffraction_order.calculate_rgb_image()
    diffraction_order.plot_all()

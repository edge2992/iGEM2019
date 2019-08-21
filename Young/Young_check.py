from Young.Young_pattern import Young_Pattern
import matplotlib.pyplot as plt


def show_list_YP(YP, width=5, height=5):
    for i in range(1, width*height+1):
        plt.subplot(width, height, i)
        plt.imshow(YP.far_generation(20), cmap='pink', vmin=0, vmax=1)
    plt.show()


def main():
    textname = "../data/save.txt"
    YP = Young_Pattern(1, 2, 1.0, -0.25, 0.08)
    # YP.init_state(50, 50)
    # show_list_YP(YP)
    YP.init_state(100, 100)
    YP.load_text(textname)
    plt.figure(figsize=(10, 10))
    plt.imshow(YP.far_generation(100), cmap='pink', vmin=0, vmax=1)
    plt.show()


if __name__ == "__main__":
    main()

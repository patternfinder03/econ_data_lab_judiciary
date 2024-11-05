from webdriver_manager.chrome import ChromeDriverManager

def install_chromedriver(version="130.0.6723.92"):
    driver_path = ChromeDriverManager(version=version).install()
    print(f"ChromeDriver {version} installed at: {driver_path}")

if __name__ == "__main__":
    install_chromedriver()

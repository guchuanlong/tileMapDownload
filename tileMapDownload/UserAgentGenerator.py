# coding: utf-8

import random
from datetime import datetime

class UserAgentGenerator:
    def __init__(self):
        self.chrome_versions = [f'12{random.randint(0, 9)}.{random.randint(0, 9)}.{random.randint(1000, 9999)}' for _ in range(5)]
        self.firefox_versions = [f'11{random.randint(0, 9)}' for _ in range(5)]
        self.safari_versions = [f'60{random.randint(0, 9)}.{random.randint(1, 9)}.{random.randint(1, 9)}' for _ in range(5)]
        self.edge_versions = [f'12{random.randint(0, 9)}.0.{random.randint(1000, 9999)}' for _ in range(5)]

        # 设备配置
        self.desktop_os = {
            'Windows': ['10.0', '11.0', '6.1', '6.2', '6.3'],
            'Macintosh': [f'Intel Mac OS X 10_{random.randint(10, 15)}_{random.randint(1, 9)}' for _ in range(5)],
            'Linux': ['x86_64', 'i686']
        }

        self.mobile_devices = {
            'iPhone': [f'iPhone{random.randint(8, 15)},{random.randint(1, 3)}' for _ in range(5)],
            'iPad': [f'iPad{random.randint(6, 10)},{random.randint(1, 3)}' for _ in range(5)],
            'Android': [f'Samsung SM-G{random.randint(900, 999)}{chr(random.randint(65, 70))}',
                        f'Pixel {random.randint(3, 7)}',
                        f'Xiaomi Mi {random.randint(9, 12)}']
        }

    def _random_version(self, versions):
        return random.choice(versions)

    def _random_os(self, os_type):
        return random.choice(self.desktop_os[os_type])

    def _random_mobile_device(self):
        device_type = random.choice(list(self.mobile_devices.keys()))
        return device_type, random.choice(self.mobile_devices[device_type])

    def generate_chrome(self):
        os_type = random.choice(['Windows', 'Macintosh', 'Linux'])
        if os_type == 'Windows':
            return f"Mozilla/5.0 (Windows NT {self._random_os('Windows')}; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/{self._random_version(self.chrome_versions)} Safari/537.36"
        elif os_type == 'Macintosh':
            return f"Mozilla/5.0 (Macintosh; {self._random_os('Macintosh')}) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/{self._random_version(self.chrome_versions)} Safari/537.36"
        else:  # Linux
            distro = random.choice(['Ubuntu', 'Fedora', 'Debian'])
            return f"Mozilla/5.0 (X11; Linux {random.choice(self.desktop_os['Linux'])}) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/{self._random_version(self.chrome_versions)} Safari/537.36"

    def generate_firefox(self):
        os_type = random.choice(['Windows', 'Macintosh', 'Linux'])
        if os_type == 'Windows':
            return f"Mozilla/5.0 (Windows NT {self._random_os('Windows')}; Win64; x64; rv:{self._random_version(self.firefox_versions)}) Gecko/20100101 Firefox/{self._random_version(self.firefox_versions)}"
        elif os_type == 'Macintosh':
            return f"Mozilla/5.0 (Macintosh; {self._random_os('Macintosh')}; rv:{self._random_version(self.firefox_versions)}) Gecko/20100101 Firefox/{self._random_version(self.firefox_versions)}"
        else:  # Linux
            return f"Mozilla/5.0 (X11; Linux {random.choice(self.desktop_os['Linux'])}; rv:{self._random_version(self.firefox_versions)}) Gecko/20100101 Firefox/{self._random_version(self.firefox_versions)}"

    def generate_safari(self):
        os_type = random.choice(['Macintosh', 'iPhone', 'iPad'])
        if os_type == 'Macintosh':
            return f"Mozilla/5.0 (Macintosh; {self._random_os('Macintosh')}) AppleWebKit/{self._random_version(self.safari_versions)} (KHTML, like Gecko) Version/{random.choice(['16.0', '16.1', '16.2', '17.0'])} Safari/{self._random_version(self.safari_versions)}"
        else:  # iPhone or iPad
            device_type, device = self._random_mobile_device()
            os_ver = f"{random.randint(15, 17)}_{random.randint(0, 3)}"
            return f"Mozilla/5.0 ({device}; CPU {device_type} OS {os_ver} like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/{random.randint(15, 17)}.0 Mobile/15E148 Safari/604.1"

    def generate_edge(self):
        chrome_ver = self._random_version(self.chrome_versions)
        edge_ver = self._random_version(self.edge_versions)
        return f"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/{chrome_ver} Safari/537.36 Edg/{edge_ver}"

    def generate_android(self):
        device = random.choice(self.mobile_devices['Android'])
        android_ver = random.choice(['10', '11', '12', '13'])
        chrome_ver = self._random_version(self.chrome_versions)
        return f"Mozilla/5.0 (Linux; Android {android_ver}; {device}) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/{chrome_ver} Mobile Safari/537.36"

    def random(self):
        """生成一个随机的User-Agent字符串"""
        browser = random.choices(
            population=['chrome', 'firefox', 'safari', 'edge', 'android'],
            weights=[0.45, 0.25, 0.15, 0.10, 0.05],  # 浏览器市场份额权重
            k=1
        )[0]

        if browser == 'chrome':
            return self.generate_chrome()
        elif browser == 'firefox':
            return self.generate_firefox()
        elif browser == 'safari':
            return self.generate_safari()
        elif browser == 'edge':
            return self.generate_edge()
        else:  # android
            return self.generate_android()

    def bulk_generate(self, count=100):
        """批量生成指定数量的User-Agent"""
        return [self.random() for _ in range(count)]


# 使用示例
if __name__ == "__main__":
    generator = UserAgentGenerator()

    # 生成单个UA
    print("随机User-Agent示例:")
    print(generator.random())

    # 批量生成100个
    print("\n生成100个User-Agent:")
    ua_list = generator.bulk_generate(100)
    for i, ua in enumerate(ua_list, 1):
        print(f"{i}. {ua}")
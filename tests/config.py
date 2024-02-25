import os

from appium.options.android import UiAutomator2Options
from dotenv import load_dotenv
from pydantic import BaseModel

from QAGuru9_22 import utils


class Config(BaseModel):
    context: str
    remote_url: str = os.getenv('REMOTE_URL')
    device_name: str = os.getenv('DEVICE_NAME')
    udid: str = os.getenv('UDID')
    appWaitActivity: str = os.getenv('APP_WAIT_ACTIVITY')
    app_local: str = utils.file.abs_path_from_project(os.getenv('APP'))
    app_bstack: str = os.getenv('APP')
    platformName: str = os.getenv('PLATFORM_NAME')
    platformVersion: str = os.getenv('PLATFORM_VERSION')
    load_dotenv(dotenv_path=utils.file.abs_path_from_project('.env.credentials'))
    userName: str = os.getenv('USER_NAME')
    accessKey: str = os.getenv('ACCESS_KEY')

    def to_android_driver_options(self, context):
        options = UiAutomator2Options()

        if context == 'local_emulator':
            options.set_capability('remote_url', self.remote_url)
            options.set_capability('udid', self.udid)
            options.set_capability('appWaitActivity', self.appWaitActivity)
            options.set_capability('app', self.app_local)

        if context == 'local_real_device':
            options.set_capability('remote_url', self.remote_url)
            options.set_capability('udid', self.udid)
            options.set_capability('appWaitActivity', self.appWaitActivity)
            options.set_capability('app', self.app_local)

        if context == 'bstack':
            options.set_capability('remote_url', self.remote_url)
            options.set_capability('deviceName', self.device_name)
            options.set_capability('platformName', self.platformName)
            options.set_capability('platformVersion', self.platformVersion)
            options.set_capability('appWaitActivity', self.appWaitActivity)
            options.set_capability('app', self.app_bstack)
            options.set_capability(
                'bstack:options', {
                    'projectName': 'Wikipedia tests project',
                    'buildName': 'Wikipedia-app-build',
                    'sessionName': 'Wikipedia tests',
                    'userName': self.userName,
                    'accessKey': self.accessKey,
                },
            )

        print(self.device_name)

        return options


config = Config(context="local_emulator")
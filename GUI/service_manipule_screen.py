import time

from collections import namedtuple
from .graphic_interface import GraphicInterface
from log.log_as_exception import LogAsException
from system.directory import Directory

class ServiceManipuleScreen(GraphicInterface):
    
    def __init__(self) -> None:
        super().__init__()
        self._log = LogAsException()
    
    def click_in_img_reference(self, img_reference):
        locate_img_reference = self.return_position_image_on_screen(img_reference)
        if locate_img_reference:
            self._screen.click(locate_img_reference)
            return True
        raise self._log.critical(f"não foi possivel clicar na imagem {img_reference}")
    
    def return_position_image_on_screen(self, img_reference):
        try:
            return self._screen.locateOnScreen(img_reference)
        except Exception as err:
            self._log.critical(err)
    
    def try_locate_image_on_screen(self, img_reference, timeout=10):
        count = 0
        while count <= timeout:
            if self.return_position_image_on_screen(img_reference):
                return True
            count += 1
            time.sleep(1)
    
    def wait_image_reference_to_vanish(self, img_reference):
        while self.return_position_image_on_screen(img_reference):
            continue
        return True
    
    def manipule_region_to_screenshot_based_in_image_reference(self, img_reference, name_screenshot, left_sum=0, top_sum=0, width_sum=0, height_sum=0):
        if self.try_locate_image_on_screen(img_reference):
            position_reference = self._screen.locateOnScreen(img_reference)
            name_positions = namedtuple("name_positions", "left top width height")
            position = name_positions(position_reference[0], position_reference[1], position_reference[2], position_reference[3])
            screenshot = self._screen.screenshot(region=(position.left + left_sum, position.top + top_sum, position.width + width_sum, position.height + height_sum))
            screenshot.save(Directory.temporary.value + name_screenshot)
            return True
        self._log.critical("não foi possivel reconhecer referencia para screenshot")
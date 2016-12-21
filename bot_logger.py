import logging

formatter = logging.Formatter('%(asctime)s %(levelname)s %(message)s')

info_logger = logging.getLogger('info_logger')
hdlr = logging.FileHandler('log/loginfo.log')
hdlr.setFormatter(formatter)
info_logger.addHandler(hdlr)
info_logger.setLevel(logging.INFO)

error_logger = logging.getLogger('erro')
hdlr_2 = logging.FileHandler('log/error.log')
hdlr_2.setFormatter(formatter)
error_logger.addHandler(hdlr_2)
error_logger.setLevel(logging.ERROR)
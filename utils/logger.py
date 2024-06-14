"""
This module provides logging functionality, cinema_logger save cinema logs in cinema.log
and transaction_logger save transaction.log file.
"""
import logging

cinema_logger = logging.getLogger('cinema_logging')
cinema_file_handler = logging.FileHandler('../cinema.log')
cinema_file_handler_format = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
cinema_file_handler.setFormatter(cinema_file_handler_format)
cinema_logger.addHandler(cinema_file_handler)
cinema_logger.setLevel(logging.INFO)

transaction_logger = logging.getLogger('transaction_logging')
transaction_file_handler = logging.FileHandler('../transaction.log')
transaction_file_handler_format = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
transaction_file_handler.setFormatter(transaction_file_handler_format)
transaction_logger.addHandler(transaction_file_handler)
transaction_logger.setLevel(logging.INFO)

const { SerialPort } = require('serialport');

const port = new SerialPort({
    path: '/dev/tty-usbserial1',
    baudRate: 57600,
  })
port.write('ROBOT POWER ON')
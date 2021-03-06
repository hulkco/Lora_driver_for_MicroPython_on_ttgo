from sx127x import sx127x
from sx127x import config

# import LoRaDumpRegisters
# import LoRaSender
# import LoRaReceiver
# import LoRaSetSpread
# import LoRaSetSyncWord
# import LoRaReceiverCallback
# import LoRaDuplex
import examples.duplex.lora_duplex as lora_duplex
# import LoRaPingPong
    
 
def main(): 
    
    # Controller(
               # pin_id_led = ON_BOARD_LED_PIN_NO, 
               # on_board_led_high_is_on = ON_BOARD_LED_HIGH_IS_ON,
               # pin_id_reset = PIN_ID_FOR_LORA_RESET, 
               # blink_on_start = (2, 0.5, 0.5))
    controller = config.get_controller()
    
    
    # SX127x(name = 'SX127x',
           # parameters = {'frequency': 433E6, 'tx_power_level': 2, 'signal_bandwidth': 125E3,
                         # 'spreading_factor': 8, 'coding_rate': 5, 'preamble_length': 8,
                         # 'implicitHeader': False, 'sync_word': 0x12, 'enable_CRC': False},
           # onReceive = None)
           
    # controller.add_transceiver(transceiver,
                               # pin_id_ss = PIN_ID_FOR_LORA_SS,
                               # pin_id_RxDone = LORA_DIO0,
                               # pin_id_RxTimeout = LORA_DIO1,
                               # pin_id_ValidHeader = LORA_DIO2,
                               # pin_id_CadDone = LORA_DIO3,
                               # pin_id_CadDetected = LORA_DIO4,
                               # pin_id_PayloadCrcError = LORA_DIO5)
    lora = controller.add_transceiver(sx127x.SX127x(name = 'LoRa', spi=controller.spi, frequency="915E6"),
                                      pin_id_ss = controller.LORA_CS,
                                      pin_id_RxDone = controller.LORA_DIO0)
    print('lora', lora)
    

    # LoRaDumpRegisters.dumpRegisters(lora)
    # LoRaSender.send(lora)    
    # LoRaReceiver.receive(lora)
    # LoRaSetSpread.setSpread(lora)
    # LoRaSetSyncWord.setSyncWord(lora)
    # LoRaReceiverCallback.receiveCallback(lora)
    # LoRaDuplex.duplex(lora)
    lora_duplex.duplex_callback(lora)
    # LoRaPingPong.ping_pong(lora)

    
if __name__ == '__main__':
    main()
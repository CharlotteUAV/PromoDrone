Promotional concept for Charlotte UAV -- PromoDrone
==============================================================
<hr>

Overview
---

* Create a Modular Information Dissemination System for a DJI Phantom 4, with the following characteristics:
    * Universal mount capability
    * Activated via existing DJI software
    * Capability to broadcast pre-recorded message with on-board speaker
    * SDR
        * Capable of transmitting in the FM band
        * Capable of executing GNURadio scripts
    * Pamphlet drop capabilities

Approach
---
* Universal mount
    * 3D printed using:
        * <XYZ>
* Activation
    * Payload choice made possible by the use of a Hak5 Rubber Ducky
        * https://hakshop.com/collections/usb-rubber-ducky
    * The ability to start and stop the payloads on demand were accomplished with the existing light system of the DJI
    * Used a <XYZ> Photoresistor as the trigger mechanism
        * Chosen based on ambient light not interferring with trigger operations
    * Used a Raspberry Pi 3 as the "Backbone" for control of the payloads
        * kali-2017.01-rpi2.img.xz
* Speaker broadcast
    * USB to 3mm audio jack
    * /root/proj/PAYLOADS/speakerSensor.py
* SDR
    * Transmission via HackRF using firmware:
        * https://github.com/mossmann/hackrf/releases/download/v2017.02.1/hackrf-2017.02.1.zip
    * GNURadio scripts based on inspiration from:
        * https://github.com/aclytle/hackrf-flowgraphs
        * /root/proj/FLOWS/wbfm_transmit.grc
    * /root/proj/PAYLOADS/hackrfSensor.py
    * /root/proj/PAYLOADS/hackrfTransmit.py
* Pamphlet drop
    * Used a <XYZ> model servo
        * Modified to do <ABC>
    * /root/proj/PAYLOADS/servoSensor.py

Caveats / Lessons Learned
---
* Raspberry Pi 3 was chosen due to it's performance/size/power-consumption ratio
    * Initially a BeagleBone Black was chosen, but the CPU was not able to keep up with the Sample Rate needed for usable FM transmission
    * Audible at 1.03 million Sample Rate
        * Buffer Underruns still happen, but the transmission is understandable and usable from a Warfighting perspective
        * Swap space was not tested as this would lead to possible degradation of the SD card
* Kali Linux Operating System
    * https://www.kali.org/
    * Well proven in the field for realiability when it comes to things like this
        * SDR
        * 802.11
    * The possibility for offensive 802.11 attacks in future releases
    * The only Python package not found in the repo was wiringpi
        * pip used as the workaround
* Operational Security
    * This release is "wide-open" in the physical sense
        * Powering on results in an X environment with root access

Future development
---
* LED operation for communication to user as to what "stage" the payload/OS is in
* LUKS Full Disk Encryption
    * Rubber Ducky chosen as ideal candidate for token based mechanism
* Rubber Ducky payload selection method
    * Rubber Ducky or other similar method would provide a GPG style token based mechanism for arming/de-arming prior to flight
    * Only an operator with the correct physical device would be able to use the provided payloads
        * Overrides would take place via console/ssh access
    * While not physical distance based, this would allow for "2-man" rule implementation
* 802.11 communication with onboard Raspberry Pi
    * EAP is possible with hostapd
    * WPA2/PSK (AES) at a minimum
* Signal jamming/SigInt capabilities via on-board HackRF
    * Multiple devices or BladeRF needed for Full-Duplex
    * HackRF well suited for amplification via small hardware
        * FM range with no amplification was found to exceed 50 yds through Sheetrock and Bricks
* Servo based mechanism allows for kinetic operation delivery




---
title: "Vevor"
---

This inverter is a cheap and cheerfull chinese built to order for vevor it can be found in various other brands. It has a SmartESS wifi adapter installed, that is well integrated in HomeAssistant. Beware that the could solution does limit datacalls, so you will experience issues if you bombard it.

The inverter has a exceptionally low start power rating (somewhere between 60-90v) so ideal for smaller installations.

It is not waterproofed, and contains fans that run continuously, uses have reported good results replacing the fans with quieter models.

## Compatible Vevor inverters

EM6200-48L 48v RS485 6kw inverter.
EM3500-24L untested beware 24v model.

## Which protocol to use

This uses an adaptation of the Pylontech protocol, original protocol supplied by vevor but several other sources and some reverse-engineering made it work.
The implementation is not perfect, it does respect stop, and 0A current, but some of the operation is still work in progress.

Tested use with Relion batteries and lilygoCANRS485.

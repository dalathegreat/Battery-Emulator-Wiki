---
title: "Vevor"
---

!!! warning "Work in progress"
    This inverter is not entirely supported by Battery-Emulator, there is no dedicated protocol for it in the Settings and it is not confirmed yet which of the existing protocols works with it. This page collects what is known so far, so it may be incomplete or untested. Can you help? See [data needed for a new inverter integration](../../setup/contributing/data_needed_for_new_inverter_integration.md).

This inverter is a cheap and cheerful Chinese built to order for Vevor it can be found in various other brands. It has a SmartESS wifi adapter installed, that is well integrated in Home Assistant. Beware that the could solution does limit data calls, so you will experience issues if you bombard it.

The inverter has a exceptionally low start power rating (somewhere between 60-90v) so ideal for smaller installations.

It is not waterproofed, and contains fans that run continuously, uses have reported good results replacing the fans with quieter models.

## Compatible Vevor inverters

EM6200-48L 48v RS485 6kw inverter.
EM3500-24L untested beware 24v model.

## Which protocol to use

This uses an adaptation of the Pylontech protocol, original protocol supplied by vevor but several other sources and some reverse-engineering made it work.
The implementation is not perfect, it does respect stop, and 0A current, but some of the operation is still work in progress.

Tested use with Relion batteries and lilygoCANRS485.

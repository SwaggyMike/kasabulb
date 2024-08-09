# KasaBulb Automation

This project automates Kasa smart lights based on specific events, such as the start of a Baltimore Orioles game. The automation is handled by Python scripts that leverage the `python-kasa` library, allowing you to customize your smart lighting to suit your preferences.

## Features

- Automate Kasa lights to turn on, off, or change colors based on predefined events or conditions.
- Integrate seamlessly with triggers like sports games or other custom events.
- Simple and customizable Python scripts to fit your unique setup.

## Prerequisites

- A Linux server (or VM) running systemd services. The scripts are designed for this environment. Personally, I run them on a VM hosted on my Unraid server.

## Getting Started

1. Clone the repository:

   ```bash
   git clone https://github.com/SwaggyMike/kasabulb.git
   ```

2. Install the required dependencies. Note that additional dependencies may be listed in the respective directories for each project:

   ```bash
   pip install python-kasa


3. Customize the scripts to fit your needs, and set them up as systemd services to automate your Kasa bulbs.

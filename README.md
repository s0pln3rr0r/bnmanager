# BNManager (BotNet Manager)

BNManager (BotNet Manager) is a powerful tool designed for managing botnets efficiently. With BNManager, you can easily create bind shells, reverse shells, operate your botnet, edit bots, and more, all through a beautiful terminal UI.

## Features

### Create Bind Shells
- Create bind shells in various languages including Python, PHP, Netcat (NC), and Perl.
- Add custom commands for persistence.
- Automatically add infected systems to our botnet.

### Create Reverse Shells
- Generate reverse shells in Python3, PHP, Netcat (NC), and Bash.
- Customize commands for persistence.
- Automatically integrate infected systems into our botnet.

### Operate Botnet
- Manage the entire botnet effortlessly.
- Execute a Distributed Denial of Service (DDoS) attack (ping of death attack) using your entire botnet.
- Control any single bot from the botnet using a custom-made BNShell.
- Send common commands to all bots simultaneously.
- Connect to reverse shells using the new listener module in [BNManager v2.0](https://github.com/s0pln3rr0r/bnmanager)

### Edit Bot
- View all bots within your botnet.
- Edit basic details of already created bots.

### Beautiful Terminal UI
- Enjoy a user-friendly terminal interface for seamless interaction with the tool.

## Getting Started

To get started with BNManager, follow these steps:

1. Clone the repository to your local machine:
    ```bash
    git clone https://github.com/s0pln3rr0r/bnmanager.git
    ```

2. Navigate to the project directory:
    ```bash
    cd bnmanager
    ```

3. Install the required dependencies:
    ```bash
    sudo bash install_requirements.sh
    ```

4. Give bnmanager.py executable permissions:
   ```bash
   chmod +x bnmanager.py
   ```
   
5. Launch BNManager:
    ```bash
    python3 bnmanager.py
    ```

## Usage

Once BNManager is running, using help menu you can navigate through the menu options to utilize its various features:

- Create bind shells or reverse shells as needed.
- Operate your botnet efficiently, perform DDoS attacks, control individual bots, and execute commands across all bots.
- Edit bot details to manage your botnet effectively.

## Contributing

Contributions are welcome! Feel free to fork the repository, make your changes, and submit a pull request.

## License

This project is licensed under the [MIT License](LICENSE). Feel free to modify and distribute it as per the terms of the license.

## Contact

If you have any questions or suggestions regarding BNManager, feel free to reach out to us at [s0pln3rr0r@proton.me](mailto:s0pln3rr0r@proton.me).

Happy botnet managing with BNManager! 🤖💻

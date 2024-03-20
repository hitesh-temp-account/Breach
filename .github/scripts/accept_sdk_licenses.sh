#!/usr/bin/expect -f

# An Expect Script to automate the Android SDK licenses agreement

# Runs 'sdkmanager --licenses' command in a new process and links below script to that process
spawn sdkmanager --licenses

expect {

    # This block expects "y/N" patterns from the linked process
    "y/N" {

        # Sends the character 'y' followed by return (\r) for the prompts in the attached process
        send "y\r"

        # Continues to wait for additional expected pattern ("y/N")
        exp_continue
    }

    # Matches with the end of output of the process
    eof
}

# Exit the script
exit

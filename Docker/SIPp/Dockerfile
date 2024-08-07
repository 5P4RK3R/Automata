# Use a base image with a compatible Linux distribution (e.g., Ubuntu)
FROM ubuntu:latest

# Install dependencies and build tools
RUN apt-get update && apt-get install -y \
    build-essential \
    libncurses5-dev \
    libssl-dev \
    libpcap-dev \
    libpcre3-dev \
    bison \
    flex

# Download and compile SIPp
WORKDIR /sipp
RUN apt-get install -y git
RUN git clone https://github.com/SIPp/sipp.git .
RUN make

# Cleanup to reduce image size
RUN apt-get remove -y git build-essential && apt-get autoremove -y && apt-get clean

# Set the default command to run SIPp
CMD ["/sipp/sipp"]

# docker run -it --rm sipp-image -sn uac <SIP_SERVER_IP>:<SIP_SERVER_PORT> -i <YOUR_IP> -p <YOUR_PORT> -sf <TEST_SCENARIO_FILE>

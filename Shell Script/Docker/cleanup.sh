#!/bin/bash

# Print a message indicating the start of cleanup
echo "Starting Docker cleanup..."

# Remove dangling images
echo "Removing dangling images..."
docker image prune -f

# Remove stopped containers
echo "Removing stopped containers..."
docker container prune -f

# Optionally, remove unused volumes
echo "Removing unused volumes..."
docker volume prune -f

# Optionally, remove unused networks
echo "Removing unused networks..."
docker network prune -f

echo "Docker cleanup completed."

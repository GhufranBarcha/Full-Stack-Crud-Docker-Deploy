# Use an official Node.js runtime as a parent image
FROM node

# Set the working directory in the container
WORKDIR /frontend

# Copy the package.json and package-lock.json to the working directory
COPY package*.json ./

# Install project dependencies
RUN npm install

# Copy the rest of the application files to the container
COPY . .

# Expose the port that the Vite server will run on (default for Vite is 5173)
EXPOSE 5173

# Command to start the Vite development server
CMD ["npm", "run", "dev"]

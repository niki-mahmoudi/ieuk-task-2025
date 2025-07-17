# uses node version that is our base image
FROM python:3.11-slim

# goes to the app directory 
WORKDIR /app

# install app dependancies
RUN npm install

COPY requirements.txt ./
RUN pip install --no-cache-dir -r requirements.txt

# copy the rest of our app into the container
COPY . .


# # set port environment variable
# ENV PORT=9000
# # expose the port so our computer can access it
# EXPOSE 9000

# run the app
CMD ["npm", "start"]
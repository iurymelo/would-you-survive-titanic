FROM node:13-alpine
COPY . /home/front/app
WORKDIR /home/front/app
ENV PATH /home/front/app/node_modules/.bin$PATH
run npm install --silent
run npm install --save react-scripts@3.3.1 -g --silent
EXPOSE 3000
CMD ["npm", "start"]

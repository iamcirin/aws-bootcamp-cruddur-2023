# Stage 1 - build the app
FROM node:16.18 AS build

ENV PORT=3000

WORKDIR /frontend-react-js
COPY . .

RUN npm install
RUN npm run build

# Stage 2 - create a smaller image for deployment
FROM node:16.18-alpine

ENV PORT=3000

WORKDIR /frontend-react-js

COPY --from=build /frontend-react-js/build /frontend-react-js/build
COPY --from=build /frontend-react-js/package.json /frontend-react-js/package.json
COPY --from=build /frontend-react-js/node_modules /frontend-react-js/node_modules

EXPOSE ${PORT}
CMD ["npm", "start"]

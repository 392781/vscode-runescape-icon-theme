FROM node:current-alpine AS node
FROM alpine:latest

COPY --from=node /usr/lib /usr/lib
COPY --from=node /usr/local/lib /usr/local/lib
COPY --from=node /usr/local/include /usr/local/include
COPY --from=node /usr/local/bin /usr/local/bin

RUN node -v
RUN apk add git openssh
RUN chown -R 1000:0 "/root/.npm" || true
RUN npm install -g yo generator-code @vscode/vsce --force

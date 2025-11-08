FROM n8nio/n8n:latest

# Install additional dependencies or custom nodes here
# RUN npm install n8n-nodes-my-custom-package

COPY ../../automation/scripts /home/node/automation-scripts
RUN chown -R node:node /home/node/automation-scripts

USER node

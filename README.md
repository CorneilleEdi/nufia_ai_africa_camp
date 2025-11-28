### Configurations

.env

```bash
export GOOGLE_API_KEY="<GOOGLE_AI_STUDIO_API_KEY>"
export GOOGLE_GENAI_USE_VERTEXAI=FALSE
export GOOGLE_GENAI_MODEL="gemini-2.5-flash-lite"
```

Google AI Studio API Key: https://aistudio.google.com/


### Deploy and Run

```bash


export GOOGLE_CLOUD_PROJECT="workstorm-a4466"
export GOOGLE_CLOUD_LOCATION="europe-west9"
export GOOGLE_GENAI_USE_VERTEXAI=FALSE
export GOOGLE_API_KEY="AIzaSyAoS5B_WYEdUmiy-xGpiwOsISi7ZoP2QRM"
export AGENT_PATH="./demo_0


adk deploy cloud_run \
--project=$GOOGLE_CLOUD_PROJECT \
--region=$GOOGLE_CLOUD_LOCATION \
--service_name=$SERVICE_NAME \
--app_name=$APP_NAME \
--with_ui \
$AGENT_PATH
```
#!/bin/bash
echo "Enter the model name (default is orca-mini): "
read model_name
[ -z "$model_name" ] && model_name="orca-mini"
ollama run $model_name

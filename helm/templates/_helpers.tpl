{{/*
Expand the name of the chart.
*/}}
{{- define "fipslogs.name" -}}
{{- default .Release.Name .Values.deploy.nameOverride | trunc 63 | trimSuffix "-" }}
{{- end }}

{{/*
Create chart name and version as used by the chart label.
*/}}
{{- define "fipslogs.chart" -}}
{{- printf "%s-%s" .Chart.Name .Chart.Version | replace "+" "_" | trunc 63 | trimSuffix "-" }}
{{- end }}

{{/*
Common labels
*/}}
{{- define "fipslogs.labels" -}}
clusterName: {{ include "fipslogs.name" . }}
helm.sh/chart: {{ include "fipslogs.chart" . }}
meta.helm.sh/release-name: {{ include "fipslogs.name" . }}
meta.helm.sh/release-namespace: {{ .Release.Namespace }}
{{- if .Chart.AppVersion }}
app.kubernetes.io/version: {{ .Chart.AppVersion | quote }}
{{- end }}
app.kubernetes.io/managed-by: {{ .Release.Service }}
{{- range .Values.deploy.resourceLabels }}
{{ .key }}: {{ .value }}
{{- end }}
{{- end }}

{{/*
Service selector labels
*/}}
{{- define "fipslogs.selectorLabels" -}}
clusterName: {{ include "fipslogs.name" . }}
app: infinispan-pod
{{- end }}
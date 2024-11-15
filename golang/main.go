package main

import(
	"net/http"
	//"time"
	"html/template"
	"log"
    "os/exec" //use this as it is easier/faster for easy kubecdtl get cmds
    "strings"
)
type PageData struct {
    Namespaces []string
    SelectedNamespace string
}

func main() {

    http.HandleFunc("/", func(w http.ResponseWriter, r *http.Request) {
        namespaces := []string {"kube-system","azure","test","default"}
        selectedNamespace := ""
		if r.Method == http.MethodPost {
			selectedNamespace = r.FormValue("namespace")
		}

		data := PageData{
			Namespaces:      namespaces,
			SelectedNamespace: selectedNamespace,
		}

		tmpl := template.Must(template.ParseFiles("templates/index.html"))
		tmpl.Execute(w, data)

        log.Printf("Selected Namespace: %s\n", selectedNamespace)
    })

    http.ListenAndServe(":8080", nil)
}

//outsource to other file
func cmdNamespace() []string{
    log.Printf("Running get Namespace Method")
    cmd := exec.Command("kubectl","get","namespaces")
    output,_ := cmd.CombinedOutput() //err is ignored by _
	namespaces := strings.Split(strings.TrimSpace(string(output)), "\n")
	return namespaces
}

func podCmd(namespace string) []string{
    cmd := exec.Command("kubectl","get","pods","-n",namespace)
    output, _ := cmd.CombinedOutput()
    pods := strings.Split(strings.TrimSpace(string(output)), "\n")
    return pods
}

func logsCmd(namespace string) string{
    cmd:= exec.Command("kubectl","logs","pods","-n",namespace)
    output, _ := cmd.CombinedOutput()
    return string(output)
}

func nodesCmd() []string{
    cmd:= exec.Command("kubectl","get","nodes")
    output, _ := cmd.CombinedOutput()
    nodes := strings.Split(strings.TrimSpace(string(output)), "\n")
    return nodes
}

func topCmd() []string{
    cmd := exec.Command("kubectl", "top", "nodes")
    output, _ := cmd.CombinedOutput()
    top := strings.Split(strings.TrimSpace(string(output)), "\n")
    return top
}



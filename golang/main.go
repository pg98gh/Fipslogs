package main

import(
	"net/http"
	//"time"
	"html/template"
	"log"
)
type PageData struct {
    Namespaces []string
}

func main() {
    namespaces := []string {"kube-system","azure","test","default"}

    http.HandleFunc("/", func(w http.ResponseWriter, r *http.Request) {
        tmpl, err := template.ParseFiles("templates/index.html")
        if err != nil {
            http.Error(w, "Unable to load template", http.StatusInternalServerError)
            return
        }
        data := PageData{
            Namespaces: namespaces,
        }

        err = tmpl.Execute(w, data)
        if err != nil {
            http.Error(w, "Failed to render template", http.StatusInternalServerError)
        }
    })
    // submit handler for "Select Namespace" form
    http.HandleFunc("/submit", func(w http.ResponseWriter, r *http.Request) {
        if r.Method != http.MethodPost {
            http.Error(w, "Invalid request method", http.StatusMethodNotAllowed)
            return
        }

        
        selectedNamespace := r.FormValue("namespace")
        log.Printf("Selected Namespace: %s\n", selectedNamespace)

        //answer to user
        w.Write([]byte("You chose: " + selectedNamespace))
    })


    log.Println("Server läuft auf http://localhost:8080")
    log.Fatal(http.ListenAndServe(":8080", nil))
}

// Grafana
resource "helm_release" "grafana" {
    name = "grafana"
    chart = "grafana"
    namespace = ""

    values = [
        "${file("../helm/grafana/values.yaml")}"
    ]

    set {
        name  = "Name"
        value = "Grafana"
    }
}

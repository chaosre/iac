// Grafana
resource "helm_release" "grafana" {
    name = "grafana"
    chart = "grafana"
    namespace = "monitoring"

    values = [
        "${file("./helm/grafana/values.yaml")}"
    ]

    set {
        name  = "Name"
        value = "Grafana"
    }
}

// Thanos
resource "helm_release" "thanos" {
    name = "thanos"
    chart = "thanos"
    namespace = "metrics"

    values = [
        "${file("./helm/thanos/values.yaml")}"
    ]

    set {
        name  = "Name"
        value = "Thanos"
    }
}
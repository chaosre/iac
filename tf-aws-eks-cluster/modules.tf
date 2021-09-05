module cluster {
    source = "./modules/cluster"
    cluster_name = var.cluster_name 
    aws_region = var.aws_region
}
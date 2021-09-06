# Terraform aws eks cluster

How to:

```bash
terraform init
```

```bash
terraform plan -out plan
```

```bash
terraform apply -auto-approve
```

### After

Update ~/.kube/config

```bash
aws eks --region us-east-1 update-kubeconfig --name k8s-generic-cluster
```

```bash
kubectl get nodes
```

## 🤝 Contributing

Contributions, issues and feature requests are welcome!<br />Feel free to check **[issues page](https://github.com/chaosre/iac/issues)**. 

## Show your support

Give a ⭐️ if this project helped you!

## 📝 License

This project is [MIT](LICENSE) licensed.

---
layout: container
name:  "quay.io/biocontainers/elastic-blast"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/elastic-blast/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/elastic-blast/container.yaml"
updated_at: "2023-05-26 02:53:07.999837"
latest: "1.0.0--pyhdfd78af_0"
container_url: "https://biocontainers.pro/tools/elastic-blast"
aliases:
 - "aws"
 - "aws-create-elastic-blast-janitor-role.sh"
 - "aws-delete-elastic-blast-janitor-role.sh"
 - "aws-describe-elastic-blast-janitor-role.sh"
 - "aws-get-auto-scaling-events.sh"
 - "aws-show-my-undeleted-searches.sh"
 - "aws.cmd"
 - "aws_bash_completer"
 - "aws_completer"
 - "aws_zsh_completer.sh"
 - "awslimitchecker"
 - "blast-tuner.py"
 - "bq"
 - "cleanup-stale-gcp-resources.py"
 - "create-blastdb-metadata.py"
 - "docker-credential-gcloud"
 - "elastic-blast"
 - "elb-cost.py"
 - "fasta_split.py"
 - "gcloud"
 - "gcp-setup-elastic-blast-janitor.sh"
 - "gcp-show-my-undeleted-searches.sh"
 - "gcp_ram_size.py"
 - "kubectl"
 - "publish.py"
 - "results2clustername.sh"
 - "gsutil"
 - "jp.py"
 - "pyrsa-decrypt"
 - "pyrsa-encrypt"
 - "pyrsa-keygen"
 - "pyrsa-priv2pub"
 - "pyrsa-sign"
 - "pyrsa-verify"
 - "rst2html4.py"
 - "rst2html5.py"
versions:
 - "0.2.7--pyhdfd78af_0"
 - "1.0.0--pyhdfd78af_0"
description: "shpc-registry automated BioContainers addition for elastic-blast"
config: {"url": "https://biocontainers.pro/tools/elastic-blast", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for elastic-blast", "latest": {"1.0.0--pyhdfd78af_0": "sha256:6991c5d12c85052f1365d81fcca48e9f3bf0b823d38226008049f0763a87b4a3"}, "tags": {"0.2.7--pyhdfd78af_0": "sha256:ea42cbd2ebc5e67f491242aca9806b69e81e59c535785d727a58e29d5f722f80", "1.0.0--pyhdfd78af_0": "sha256:6991c5d12c85052f1365d81fcca48e9f3bf0b823d38226008049f0763a87b4a3"}, "docker": "quay.io/biocontainers/elastic-blast", "aliases": {"aws": "/usr/local/bin/aws", "aws-create-elastic-blast-janitor-role.sh": "/usr/local/bin/aws-create-elastic-blast-janitor-role.sh", "aws-delete-elastic-blast-janitor-role.sh": "/usr/local/bin/aws-delete-elastic-blast-janitor-role.sh", "aws-describe-elastic-blast-janitor-role.sh": "/usr/local/bin/aws-describe-elastic-blast-janitor-role.sh", "aws-get-auto-scaling-events.sh": "/usr/local/bin/aws-get-auto-scaling-events.sh", "aws-show-my-undeleted-searches.sh": "/usr/local/bin/aws-show-my-undeleted-searches.sh", "aws.cmd": "/usr/local/bin/aws.cmd", "aws_bash_completer": "/usr/local/bin/aws_bash_completer", "aws_completer": "/usr/local/bin/aws_completer", "aws_zsh_completer.sh": "/usr/local/bin/aws_zsh_completer.sh", "awslimitchecker": "/usr/local/bin/awslimitchecker", "blast-tuner.py": "/usr/local/bin/blast-tuner.py", "bq": "/usr/local/bin/bq", "cleanup-stale-gcp-resources.py": "/usr/local/bin/cleanup-stale-gcp-resources.py", "create-blastdb-metadata.py": "/usr/local/bin/create-blastdb-metadata.py", "docker-credential-gcloud": "/usr/local/bin/docker-credential-gcloud", "elastic-blast": "/usr/local/bin/elastic-blast", "elb-cost.py": "/usr/local/bin/elb-cost.py", "fasta_split.py": "/usr/local/bin/fasta_split.py", "gcloud": "/usr/local/bin/gcloud", "gcp-setup-elastic-blast-janitor.sh": "/usr/local/bin/gcp-setup-elastic-blast-janitor.sh", "gcp-show-my-undeleted-searches.sh": "/usr/local/bin/gcp-show-my-undeleted-searches.sh", "gcp_ram_size.py": "/usr/local/bin/gcp_ram_size.py", "kubectl": "/usr/local/bin/kubectl", "publish.py": "/usr/local/bin/publish.py", "results2clustername.sh": "/usr/local/bin/results2clustername.sh", "gsutil": "/usr/local/bin/gsutil", "jp.py": "/usr/local/bin/jp.py", "pyrsa-decrypt": "/usr/local/bin/pyrsa-decrypt", "pyrsa-encrypt": "/usr/local/bin/pyrsa-encrypt", "pyrsa-keygen": "/usr/local/bin/pyrsa-keygen", "pyrsa-priv2pub": "/usr/local/bin/pyrsa-priv2pub", "pyrsa-sign": "/usr/local/bin/pyrsa-sign", "pyrsa-verify": "/usr/local/bin/pyrsa-verify", "rst2html4.py": "/usr/local/bin/rst2html4.py", "rst2html5.py": "/usr/local/bin/rst2html5.py"}}
---

This module is a singularity container wrapper for quay.io/biocontainers/elastic-blast.
shpc-registry automated BioContainers addition for elastic-blast
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/elastic-blast
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/elastic-blast:1.0.0--pyhdfd78af_0
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/elastic-blast/1.0.0--pyhdfd78af_0
$ module help quay.io/biocontainers/elastic-blast/1.0.0--pyhdfd78af_0
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### elastic-blast-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### elastic-blast-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### elastic-blast-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### elastic-blast-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### elastic-blast-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### elastic-blast-inspect-deffile:

```bash
$ singularity inspect -d <container>
```


#### aws

```bash
$ singularity exec <container> /usr/local/bin/aws
$ podman run --it --rm --entrypoint /usr/local/bin/aws   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/aws   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### aws-create-elastic-blast-janitor-role.sh

```bash
$ singularity exec <container> /usr/local/bin/aws-create-elastic-blast-janitor-role.sh
$ podman run --it --rm --entrypoint /usr/local/bin/aws-create-elastic-blast-janitor-role.sh   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/aws-create-elastic-blast-janitor-role.sh   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### aws-delete-elastic-blast-janitor-role.sh

```bash
$ singularity exec <container> /usr/local/bin/aws-delete-elastic-blast-janitor-role.sh
$ podman run --it --rm --entrypoint /usr/local/bin/aws-delete-elastic-blast-janitor-role.sh   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/aws-delete-elastic-blast-janitor-role.sh   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### aws-describe-elastic-blast-janitor-role.sh

```bash
$ singularity exec <container> /usr/local/bin/aws-describe-elastic-blast-janitor-role.sh
$ podman run --it --rm --entrypoint /usr/local/bin/aws-describe-elastic-blast-janitor-role.sh   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/aws-describe-elastic-blast-janitor-role.sh   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### aws-get-auto-scaling-events.sh

```bash
$ singularity exec <container> /usr/local/bin/aws-get-auto-scaling-events.sh
$ podman run --it --rm --entrypoint /usr/local/bin/aws-get-auto-scaling-events.sh   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/aws-get-auto-scaling-events.sh   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### aws-show-my-undeleted-searches.sh

```bash
$ singularity exec <container> /usr/local/bin/aws-show-my-undeleted-searches.sh
$ podman run --it --rm --entrypoint /usr/local/bin/aws-show-my-undeleted-searches.sh   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/aws-show-my-undeleted-searches.sh   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### aws.cmd

```bash
$ singularity exec <container> /usr/local/bin/aws.cmd
$ podman run --it --rm --entrypoint /usr/local/bin/aws.cmd   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/aws.cmd   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### aws_bash_completer

```bash
$ singularity exec <container> /usr/local/bin/aws_bash_completer
$ podman run --it --rm --entrypoint /usr/local/bin/aws_bash_completer   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/aws_bash_completer   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### aws_completer

```bash
$ singularity exec <container> /usr/local/bin/aws_completer
$ podman run --it --rm --entrypoint /usr/local/bin/aws_completer   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/aws_completer   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### aws_zsh_completer.sh

```bash
$ singularity exec <container> /usr/local/bin/aws_zsh_completer.sh
$ podman run --it --rm --entrypoint /usr/local/bin/aws_zsh_completer.sh   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/aws_zsh_completer.sh   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### awslimitchecker

```bash
$ singularity exec <container> /usr/local/bin/awslimitchecker
$ podman run --it --rm --entrypoint /usr/local/bin/awslimitchecker   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/awslimitchecker   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### blast-tuner.py

```bash
$ singularity exec <container> /usr/local/bin/blast-tuner.py
$ podman run --it --rm --entrypoint /usr/local/bin/blast-tuner.py   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/blast-tuner.py   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### bq

```bash
$ singularity exec <container> /usr/local/bin/bq
$ podman run --it --rm --entrypoint /usr/local/bin/bq   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/bq   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### cleanup-stale-gcp-resources.py

```bash
$ singularity exec <container> /usr/local/bin/cleanup-stale-gcp-resources.py
$ podman run --it --rm --entrypoint /usr/local/bin/cleanup-stale-gcp-resources.py   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/cleanup-stale-gcp-resources.py   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### create-blastdb-metadata.py

```bash
$ singularity exec <container> /usr/local/bin/create-blastdb-metadata.py
$ podman run --it --rm --entrypoint /usr/local/bin/create-blastdb-metadata.py   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/create-blastdb-metadata.py   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### docker-credential-gcloud

```bash
$ singularity exec <container> /usr/local/bin/docker-credential-gcloud
$ podman run --it --rm --entrypoint /usr/local/bin/docker-credential-gcloud   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/docker-credential-gcloud   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### elastic-blast

```bash
$ singularity exec <container> /usr/local/bin/elastic-blast
$ podman run --it --rm --entrypoint /usr/local/bin/elastic-blast   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/elastic-blast   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### elb-cost.py

```bash
$ singularity exec <container> /usr/local/bin/elb-cost.py
$ podman run --it --rm --entrypoint /usr/local/bin/elb-cost.py   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/elb-cost.py   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### fasta_split.py

```bash
$ singularity exec <container> /usr/local/bin/fasta_split.py
$ podman run --it --rm --entrypoint /usr/local/bin/fasta_split.py   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/fasta_split.py   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### gcloud

```bash
$ singularity exec <container> /usr/local/bin/gcloud
$ podman run --it --rm --entrypoint /usr/local/bin/gcloud   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/gcloud   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### gcp-setup-elastic-blast-janitor.sh

```bash
$ singularity exec <container> /usr/local/bin/gcp-setup-elastic-blast-janitor.sh
$ podman run --it --rm --entrypoint /usr/local/bin/gcp-setup-elastic-blast-janitor.sh   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/gcp-setup-elastic-blast-janitor.sh   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### gcp-show-my-undeleted-searches.sh

```bash
$ singularity exec <container> /usr/local/bin/gcp-show-my-undeleted-searches.sh
$ podman run --it --rm --entrypoint /usr/local/bin/gcp-show-my-undeleted-searches.sh   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/gcp-show-my-undeleted-searches.sh   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### gcp_ram_size.py

```bash
$ singularity exec <container> /usr/local/bin/gcp_ram_size.py
$ podman run --it --rm --entrypoint /usr/local/bin/gcp_ram_size.py   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/gcp_ram_size.py   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### kubectl

```bash
$ singularity exec <container> /usr/local/bin/kubectl
$ podman run --it --rm --entrypoint /usr/local/bin/kubectl   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/kubectl   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### publish.py

```bash
$ singularity exec <container> /usr/local/bin/publish.py
$ podman run --it --rm --entrypoint /usr/local/bin/publish.py   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/publish.py   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### results2clustername.sh

```bash
$ singularity exec <container> /usr/local/bin/results2clustername.sh
$ podman run --it --rm --entrypoint /usr/local/bin/results2clustername.sh   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/results2clustername.sh   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### gsutil

```bash
$ singularity exec <container> /usr/local/bin/gsutil
$ podman run --it --rm --entrypoint /usr/local/bin/gsutil   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/gsutil   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### jp.py

```bash
$ singularity exec <container> /usr/local/bin/jp.py
$ podman run --it --rm --entrypoint /usr/local/bin/jp.py   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/jp.py   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### pyrsa-decrypt

```bash
$ singularity exec <container> /usr/local/bin/pyrsa-decrypt
$ podman run --it --rm --entrypoint /usr/local/bin/pyrsa-decrypt   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/pyrsa-decrypt   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### pyrsa-encrypt

```bash
$ singularity exec <container> /usr/local/bin/pyrsa-encrypt
$ podman run --it --rm --entrypoint /usr/local/bin/pyrsa-encrypt   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/pyrsa-encrypt   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### pyrsa-keygen

```bash
$ singularity exec <container> /usr/local/bin/pyrsa-keygen
$ podman run --it --rm --entrypoint /usr/local/bin/pyrsa-keygen   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/pyrsa-keygen   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### pyrsa-priv2pub

```bash
$ singularity exec <container> /usr/local/bin/pyrsa-priv2pub
$ podman run --it --rm --entrypoint /usr/local/bin/pyrsa-priv2pub   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/pyrsa-priv2pub   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### pyrsa-sign

```bash
$ singularity exec <container> /usr/local/bin/pyrsa-sign
$ podman run --it --rm --entrypoint /usr/local/bin/pyrsa-sign   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/pyrsa-sign   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### pyrsa-verify

```bash
$ singularity exec <container> /usr/local/bin/pyrsa-verify
$ podman run --it --rm --entrypoint /usr/local/bin/pyrsa-verify   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/pyrsa-verify   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### rst2html4.py

```bash
$ singularity exec <container> /usr/local/bin/rst2html4.py
$ podman run --it --rm --entrypoint /usr/local/bin/rst2html4.py   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/rst2html4.py   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### rst2html5.py

```bash
$ singularity exec <container> /usr/local/bin/rst2html5.py
$ podman run --it --rm --entrypoint /usr/local/bin/rst2html5.py   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/rst2html5.py   -v ${PWD} -w ${PWD} <container> -c " $@"
```



In the above, the `<container>` directive will reference an actual container provided
by the module, for the version you have chosen to load. An environment file in the
module folder will also be bound. Note that although a container
might provide custom commands, every container exposes unique exec, shell, run, and
inspect aliases. For anycommands above, you can export:

 - SINGULARITY_OPTS: to define custom options for singularity (e.g., --debug)
 - SINGULARITY_COMMAND_OPTS: to define custom options for the command (e.g., -b)
 - PODMAN_OPTS: to define custom options for podman or docker
 - PODMAN_COMMAND_OPTS: to define custom options for the command

<br>

### Install

You can install shpc locally (for yourself or your user base) as follows:

```bash
$ git clone https://github.com/singularityhub/singularity-hpc
$ cd singularity-hpc
$ pip install -e .
```

Have any questions, or want to request a new module or version? [ask for help!](https://github.com/singularityhub/singularity-hpc/issues)
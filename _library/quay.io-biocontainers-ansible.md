---
layout: container
name:  "quay.io/biocontainers/ansible"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/ansible/container.yaml"
config_url: "https://raw.githubusercontent.com//singularityhub/shpc-registry/main/quay.io/biocontainers/ansible/container.yaml"
updated_at: "2022-10-27 01:07:38.457985"
latest: "1.9.4--py27_0"
container_url: "https://biocontainers.pro/tools/ansible"
aliases:
 - "ansible"
 - "ansible-doc"
 - "ansible-galaxy"
 - "ansible-playbook"
 - "ansible-pull"
 - "ansible-vault"
 - "smtpd.pyc"
versions:
 - "1.9.4--py27_0"
description: "shpc-registry automated BioContainers addition for ansible"
config: {"url": "https://biocontainers.pro/tools/ansible", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for ansible", "latest": {"1.9.4--py27_0": "sha256:37a18bea8ceb6152bc16d08666146067ae8a6012214d5d45b3e4f6344df6ceef"}, "tags": {"1.9.4--py27_0": "sha256:37a18bea8ceb6152bc16d08666146067ae8a6012214d5d45b3e4f6344df6ceef"}, "docker": "quay.io/biocontainers/ansible", "aliases": {"ansible": "/usr/local/bin/ansible", "ansible-doc": "/usr/local/bin/ansible-doc", "ansible-galaxy": "/usr/local/bin/ansible-galaxy", "ansible-playbook": "/usr/local/bin/ansible-playbook", "ansible-pull": "/usr/local/bin/ansible-pull", "ansible-vault": "/usr/local/bin/ansible-vault", "smtpd.pyc": "/usr/local/bin/smtpd.pyc"}}
---

This module is a singularity container wrapper for quay.io/biocontainers/ansible.
shpc-registry automated BioContainers addition for ansible
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/ansible
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/ansible:1.9.4--py27_0
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/ansible/1.9.4--py27_0
$ module help quay.io/biocontainers/ansible/1.9.4--py27_0
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### ansible-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### ansible-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### ansible-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### ansible-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### ansible-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### ansible-inspect-deffile:

```bash
$ singularity inspect -d <container>
```


#### ansible

```bash
$ singularity exec <container> /usr/local/bin/ansible
$ podman run --it --rm --entrypoint /usr/local/bin/ansible   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/ansible   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### ansible-doc

```bash
$ singularity exec <container> /usr/local/bin/ansible-doc
$ podman run --it --rm --entrypoint /usr/local/bin/ansible-doc   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/ansible-doc   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### ansible-galaxy

```bash
$ singularity exec <container> /usr/local/bin/ansible-galaxy
$ podman run --it --rm --entrypoint /usr/local/bin/ansible-galaxy   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/ansible-galaxy   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### ansible-playbook

```bash
$ singularity exec <container> /usr/local/bin/ansible-playbook
$ podman run --it --rm --entrypoint /usr/local/bin/ansible-playbook   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/ansible-playbook   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### ansible-pull

```bash
$ singularity exec <container> /usr/local/bin/ansible-pull
$ podman run --it --rm --entrypoint /usr/local/bin/ansible-pull   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/ansible-pull   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### ansible-vault

```bash
$ singularity exec <container> /usr/local/bin/ansible-vault
$ podman run --it --rm --entrypoint /usr/local/bin/ansible-vault   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/ansible-vault   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### smtpd.pyc

```bash
$ singularity exec <container> /usr/local/bin/smtpd.pyc
$ podman run --it --rm --entrypoint /usr/local/bin/smtpd.pyc   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/smtpd.pyc   -v ${PWD} -w ${PWD} <container> -c " $@"
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
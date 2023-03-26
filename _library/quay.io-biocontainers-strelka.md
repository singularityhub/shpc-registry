---
layout: container
name:  "quay.io/biocontainers/strelka"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/strelka/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/strelka/container.yaml"
updated_at: "2023-03-26 02:45:41.441957"
latest: "2.9.10--h9ee0642_1"
container_url: "https://biocontainers.pro/tools/strelka"
aliases:
 - "configureStrelkaGermlineWorkflow.py"
 - "configureStrelkaSomaticWorkflow.py"
 - "runStrelkaGermlineWorkflowDemo.bash"
 - "runStrelkaSomaticWorkflowDemo.bash"
 - "python2-config"
 - "python2.7-config"
 - "python2"
 - "python2.7"
 - "idle"
 - "python-config"
 - "smtpd.py"
versions:
 - "2.9.7--0"
 - "2.9.10--h9ee0642_1"
description: "shpc-registry automated BioContainers addition for strelka"
config: {"url": "https://biocontainers.pro/tools/strelka", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for strelka", "latest": {"2.9.10--h9ee0642_1": "sha256:e6133fa935d444aaf3aa04b57256a580d9b3498298fc17cb5f4a9818116105ec"}, "tags": {"2.9.7--0": "sha256:ba0d975925ce7d277b2e6886bd98fe0e9c9e70172d2784350605ef74b547fef3", "2.9.10--h9ee0642_1": "sha256:e6133fa935d444aaf3aa04b57256a580d9b3498298fc17cb5f4a9818116105ec"}, "docker": "quay.io/biocontainers/strelka", "aliases": {"configureStrelkaGermlineWorkflow.py": "/usr/local/bin/configureStrelkaGermlineWorkflow.py", "configureStrelkaSomaticWorkflow.py": "/usr/local/bin/configureStrelkaSomaticWorkflow.py", "runStrelkaGermlineWorkflowDemo.bash": "/usr/local/bin/runStrelkaGermlineWorkflowDemo.bash", "runStrelkaSomaticWorkflowDemo.bash": "/usr/local/bin/runStrelkaSomaticWorkflowDemo.bash", "python2-config": "/usr/local/bin/python2-config", "python2.7-config": "/usr/local/bin/python2.7-config", "python2": "/usr/local/bin/python2", "python2.7": "/usr/local/bin/python2.7", "idle": "/usr/local/bin/idle", "python-config": "/usr/local/bin/python-config", "smtpd.py": "/usr/local/bin/smtpd.py"}}
---

This module is a singularity container wrapper for quay.io/biocontainers/strelka.
shpc-registry automated BioContainers addition for strelka
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/strelka
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/strelka:2.9.10--h9ee0642_1
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/strelka/2.9.10--h9ee0642_1
$ module help quay.io/biocontainers/strelka/2.9.10--h9ee0642_1
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### strelka-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### strelka-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### strelka-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### strelka-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### strelka-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### strelka-inspect-deffile:

```bash
$ singularity inspect -d <container>
```


#### configureStrelkaGermlineWorkflow.py

```bash
$ singularity exec <container> /usr/local/bin/configureStrelkaGermlineWorkflow.py
$ podman run --it --rm --entrypoint /usr/local/bin/configureStrelkaGermlineWorkflow.py   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/configureStrelkaGermlineWorkflow.py   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### configureStrelkaSomaticWorkflow.py

```bash
$ singularity exec <container> /usr/local/bin/configureStrelkaSomaticWorkflow.py
$ podman run --it --rm --entrypoint /usr/local/bin/configureStrelkaSomaticWorkflow.py   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/configureStrelkaSomaticWorkflow.py   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### runStrelkaGermlineWorkflowDemo.bash

```bash
$ singularity exec <container> /usr/local/bin/runStrelkaGermlineWorkflowDemo.bash
$ podman run --it --rm --entrypoint /usr/local/bin/runStrelkaGermlineWorkflowDemo.bash   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/runStrelkaGermlineWorkflowDemo.bash   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### runStrelkaSomaticWorkflowDemo.bash

```bash
$ singularity exec <container> /usr/local/bin/runStrelkaSomaticWorkflowDemo.bash
$ podman run --it --rm --entrypoint /usr/local/bin/runStrelkaSomaticWorkflowDemo.bash   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/runStrelkaSomaticWorkflowDemo.bash   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### python2-config

```bash
$ singularity exec <container> /usr/local/bin/python2-config
$ podman run --it --rm --entrypoint /usr/local/bin/python2-config   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/python2-config   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### python2.7-config

```bash
$ singularity exec <container> /usr/local/bin/python2.7-config
$ podman run --it --rm --entrypoint /usr/local/bin/python2.7-config   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/python2.7-config   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### python2

```bash
$ singularity exec <container> /usr/local/bin/python2
$ podman run --it --rm --entrypoint /usr/local/bin/python2   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/python2   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### python2.7

```bash
$ singularity exec <container> /usr/local/bin/python2.7
$ podman run --it --rm --entrypoint /usr/local/bin/python2.7   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/python2.7   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### idle

```bash
$ singularity exec <container> /usr/local/bin/idle
$ podman run --it --rm --entrypoint /usr/local/bin/idle   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/idle   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### python-config

```bash
$ singularity exec <container> /usr/local/bin/python-config
$ podman run --it --rm --entrypoint /usr/local/bin/python-config   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/python-config   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### smtpd.py

```bash
$ singularity exec <container> /usr/local/bin/smtpd.py
$ podman run --it --rm --entrypoint /usr/local/bin/smtpd.py   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/smtpd.py   -v ${PWD} -w ${PWD} <container> -c " $@"
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
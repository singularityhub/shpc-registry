---
layout: container
name:  "quay.io/biocontainers/ipyrad"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/ipyrad/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/ipyrad/container.yaml"
updated_at: "2024-07-15 03:12:14.567625"
latest: "0.9.96--pyh7e72e81_0"
container_url: "https://biocontainers.pro/tools/ipyrad"
aliases:
 - "ipcluster"
 - "ipcontroller"
 - "ipengine"
 - "ipyrad"
 - "mpichversion"
 - "mpivars"
 - "parkill"
 - "hydra_nameserver"
 - "hydra_persist"
 - "hydra_pmi_proxy"
 - "mpiexec.hydra"
 - "cutadapt"
 - "vsearch"
 - "jupyter-kernel"
versions:
 - "0.9.8--py_0"
 - "0.9.66--pyh3252c3a_0"
 - "0.9.94--pyh7cba7a3_0"
 - "0.9.95--pyh7cba7a3_0"
 - "0.9.96--pyh7e72e81_0"
description: "shpc-registry automated BioContainers addition for ipyrad"
config: {"url": "https://biocontainers.pro/tools/ipyrad", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for ipyrad", "latest": {"0.9.96--pyh7e72e81_0": "sha256:36df38ee1502f3ced29f44e207484b66d59f60880082942a039bbb3f8f7c9717"}, "tags": {"0.9.8--py_0": "sha256:ef4c19a2e963d9862cec2639a71404738d83e0352b61c0c6ed270516ec34479c", "0.9.66--pyh3252c3a_0": "sha256:47646e1b0c74073a16d3033a9176ea6e651dad555aae4e7fe102eef81e4f29c2", "0.9.94--pyh7cba7a3_0": "sha256:eac5aae085a8a8ebc91cba55ca8ef00f0b3bd0561040df970a9093f8fef34ed6", "0.9.95--pyh7cba7a3_0": "sha256:ef6d8d8ad0302b1555b3a25745ebf14db8d36bb08f174c7a5c48dbbb4210a104", "0.9.96--pyh7e72e81_0": "sha256:36df38ee1502f3ced29f44e207484b66d59f60880082942a039bbb3f8f7c9717"}, "docker": "quay.io/biocontainers/ipyrad", "aliases": {"ipcluster": "/usr/local/bin/ipcluster", "ipcontroller": "/usr/local/bin/ipcontroller", "ipengine": "/usr/local/bin/ipengine", "ipyrad": "/usr/local/bin/ipyrad", "mpichversion": "/usr/local/bin/mpichversion", "mpivars": "/usr/local/bin/mpivars", "parkill": "/usr/local/bin/parkill", "hydra_nameserver": "/usr/local/bin/hydra_nameserver", "hydra_persist": "/usr/local/bin/hydra_persist", "hydra_pmi_proxy": "/usr/local/bin/hydra_pmi_proxy", "mpiexec.hydra": "/usr/local/bin/mpiexec.hydra", "cutadapt": "/usr/local/bin/cutadapt", "vsearch": "/usr/local/bin/vsearch", "jupyter-kernel": "/usr/local/bin/jupyter-kernel"}}
---

This module is a singularity container wrapper for quay.io/biocontainers/ipyrad.
shpc-registry automated BioContainers addition for ipyrad
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/ipyrad
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/ipyrad:0.9.96--pyh7e72e81_0
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/ipyrad/0.9.96--pyh7e72e81_0
$ module help quay.io/biocontainers/ipyrad/0.9.96--pyh7e72e81_0
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### ipyrad-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### ipyrad-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### ipyrad-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### ipyrad-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### ipyrad-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### ipyrad-inspect-deffile:

```bash
$ singularity inspect -d <container>
```


#### ipcluster

```bash
$ singularity exec <container> /usr/local/bin/ipcluster
$ podman run --it --rm --entrypoint /usr/local/bin/ipcluster   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/ipcluster   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### ipcontroller

```bash
$ singularity exec <container> /usr/local/bin/ipcontroller
$ podman run --it --rm --entrypoint /usr/local/bin/ipcontroller   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/ipcontroller   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### ipengine

```bash
$ singularity exec <container> /usr/local/bin/ipengine
$ podman run --it --rm --entrypoint /usr/local/bin/ipengine   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/ipengine   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### ipyrad

```bash
$ singularity exec <container> /usr/local/bin/ipyrad
$ podman run --it --rm --entrypoint /usr/local/bin/ipyrad   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/ipyrad   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### mpichversion

```bash
$ singularity exec <container> /usr/local/bin/mpichversion
$ podman run --it --rm --entrypoint /usr/local/bin/mpichversion   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/mpichversion   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### mpivars

```bash
$ singularity exec <container> /usr/local/bin/mpivars
$ podman run --it --rm --entrypoint /usr/local/bin/mpivars   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/mpivars   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### parkill

```bash
$ singularity exec <container> /usr/local/bin/parkill
$ podman run --it --rm --entrypoint /usr/local/bin/parkill   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/parkill   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### hydra_nameserver

```bash
$ singularity exec <container> /usr/local/bin/hydra_nameserver
$ podman run --it --rm --entrypoint /usr/local/bin/hydra_nameserver   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/hydra_nameserver   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### hydra_persist

```bash
$ singularity exec <container> /usr/local/bin/hydra_persist
$ podman run --it --rm --entrypoint /usr/local/bin/hydra_persist   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/hydra_persist   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### hydra_pmi_proxy

```bash
$ singularity exec <container> /usr/local/bin/hydra_pmi_proxy
$ podman run --it --rm --entrypoint /usr/local/bin/hydra_pmi_proxy   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/hydra_pmi_proxy   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### mpiexec.hydra

```bash
$ singularity exec <container> /usr/local/bin/mpiexec.hydra
$ podman run --it --rm --entrypoint /usr/local/bin/mpiexec.hydra   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/mpiexec.hydra   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### cutadapt

```bash
$ singularity exec <container> /usr/local/bin/cutadapt
$ podman run --it --rm --entrypoint /usr/local/bin/cutadapt   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/cutadapt   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### vsearch

```bash
$ singularity exec <container> /usr/local/bin/vsearch
$ podman run --it --rm --entrypoint /usr/local/bin/vsearch   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/vsearch   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### jupyter-kernel

```bash
$ singularity exec <container> /usr/local/bin/jupyter-kernel
$ podman run --it --rm --entrypoint /usr/local/bin/jupyter-kernel   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/jupyter-kernel   -v ${PWD} -w ${PWD} <container> -c " $@"
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
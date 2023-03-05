---
layout: container
name:  "quay.io/biocontainers/isoquant"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/isoquant/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/isoquant/container.yaml"
updated_at: "2023-03-05 03:46:42.293430"
latest: "3.1.2--hdfd78af_1"
container_url: "https://biocontainers.pro/tools/isoquant"
aliases:
 - "isoquant.py"
 - "gffutils-cli"
 - "activate-global-python-argcomplete"
 - "python-argcomplete-check-easy-install-script"
 - "python-argcomplete-tcsh"
 - "register-python-argcomplete"
 - "vcf_sample_filter.py"
 - "vcf_filter.py"
 - "vcf_melt"
 - "faidx"
 - "sdust"
versions:
 - "3.0.1--hdfd78af_0"
 - "3.0.3--hdfd78af_0"
 - "3.1.1--hdfd78af_0"
 - "3.1.2--hdfd78af_1"
description: "shpc-registry automated BioContainers addition for isoquant"
config: {"url": "https://biocontainers.pro/tools/isoquant", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for isoquant", "latest": {"3.1.2--hdfd78af_1": "sha256:8de4b8f333b454409344028cef8080f0dfea838f471d6da2097f3d4d35ab6132"}, "tags": {"3.0.1--hdfd78af_0": "sha256:b4cfdf3f56901d6ab9d5e38a56b33e0f08dc7b74195ef3acf38bba0e919d783d", "3.0.3--hdfd78af_0": "sha256:dbfcb8618b911ca598439d7a6a62c18c576993066a898350d6efd360cab89a7f", "3.1.1--hdfd78af_0": "sha256:146d14941cfddf579b2ba142df981d055e677d4b0508107502e16aa6a51e6f9f", "3.1.2--hdfd78af_1": "sha256:8de4b8f333b454409344028cef8080f0dfea838f471d6da2097f3d4d35ab6132"}, "docker": "quay.io/biocontainers/isoquant", "aliases": {"isoquant.py": "/usr/local/bin/isoquant.py", "gffutils-cli": "/usr/local/bin/gffutils-cli", "activate-global-python-argcomplete": "/usr/local/bin/activate-global-python-argcomplete", "python-argcomplete-check-easy-install-script": "/usr/local/bin/python-argcomplete-check-easy-install-script", "python-argcomplete-tcsh": "/usr/local/bin/python-argcomplete-tcsh", "register-python-argcomplete": "/usr/local/bin/register-python-argcomplete", "vcf_sample_filter.py": "/usr/local/bin/vcf_sample_filter.py", "vcf_filter.py": "/usr/local/bin/vcf_filter.py", "vcf_melt": "/usr/local/bin/vcf_melt", "faidx": "/usr/local/bin/faidx", "sdust": "/usr/local/bin/sdust"}}
---

This module is a singularity container wrapper for quay.io/biocontainers/isoquant.
shpc-registry automated BioContainers addition for isoquant
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/isoquant
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/isoquant:3.1.2--hdfd78af_1
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/isoquant/3.1.2--hdfd78af_1
$ module help quay.io/biocontainers/isoquant/3.1.2--hdfd78af_1
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### isoquant-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### isoquant-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### isoquant-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### isoquant-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### isoquant-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### isoquant-inspect-deffile:

```bash
$ singularity inspect -d <container>
```


#### isoquant.py

```bash
$ singularity exec <container> /usr/local/bin/isoquant.py
$ podman run --it --rm --entrypoint /usr/local/bin/isoquant.py   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/isoquant.py   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### gffutils-cli

```bash
$ singularity exec <container> /usr/local/bin/gffutils-cli
$ podman run --it --rm --entrypoint /usr/local/bin/gffutils-cli   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/gffutils-cli   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### activate-global-python-argcomplete

```bash
$ singularity exec <container> /usr/local/bin/activate-global-python-argcomplete
$ podman run --it --rm --entrypoint /usr/local/bin/activate-global-python-argcomplete   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/activate-global-python-argcomplete   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### python-argcomplete-check-easy-install-script

```bash
$ singularity exec <container> /usr/local/bin/python-argcomplete-check-easy-install-script
$ podman run --it --rm --entrypoint /usr/local/bin/python-argcomplete-check-easy-install-script   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/python-argcomplete-check-easy-install-script   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### python-argcomplete-tcsh

```bash
$ singularity exec <container> /usr/local/bin/python-argcomplete-tcsh
$ podman run --it --rm --entrypoint /usr/local/bin/python-argcomplete-tcsh   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/python-argcomplete-tcsh   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### register-python-argcomplete

```bash
$ singularity exec <container> /usr/local/bin/register-python-argcomplete
$ podman run --it --rm --entrypoint /usr/local/bin/register-python-argcomplete   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/register-python-argcomplete   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### vcf_sample_filter.py

```bash
$ singularity exec <container> /usr/local/bin/vcf_sample_filter.py
$ podman run --it --rm --entrypoint /usr/local/bin/vcf_sample_filter.py   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/vcf_sample_filter.py   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### vcf_filter.py

```bash
$ singularity exec <container> /usr/local/bin/vcf_filter.py
$ podman run --it --rm --entrypoint /usr/local/bin/vcf_filter.py   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/vcf_filter.py   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### vcf_melt

```bash
$ singularity exec <container> /usr/local/bin/vcf_melt
$ podman run --it --rm --entrypoint /usr/local/bin/vcf_melt   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/vcf_melt   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### faidx

```bash
$ singularity exec <container> /usr/local/bin/faidx
$ podman run --it --rm --entrypoint /usr/local/bin/faidx   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/faidx   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### sdust

```bash
$ singularity exec <container> /usr/local/bin/sdust
$ podman run --it --rm --entrypoint /usr/local/bin/sdust   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/sdust   -v ${PWD} -w ${PWD} <container> -c " $@"
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
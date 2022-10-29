---
layout: container
name:  "quay.io/biocontainers/taranis"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/taranis/container.yaml"
config_url: "https://raw.githubusercontent.com//singularityhub/shpc-registry/main/quay.io/biocontainers/taranis/container.yaml"
updated_at: "2022-10-29 05:33:46.846646"
latest: "2.0.1--hdfd78af_0"
container_url: "https://biocontainers.pro/tools/taranis"
aliases:
 - "Dockerfile"
 - "allele_calling.py"
 - "analyze_schema.py"
 - "create_schema.py"
 - "distance_matrix.py"
 - "environment.yml"
 - "logging_config.ini"
 - "reference_alleles.py"
 - "taranis.py"
 - "taranis_configuration.py"
 - "2to3-3.7"
 - "CA.pm"
 - "LICENSE"
 - "SOAPsh.pl"
 - "accn-at-a-time"
 - "ace.pl"
 - "acyclic"
 - "alimask"
 - "amino-acid-composition"
 - "annotate"
versions:
 - "2.0.1--hdfd78af_0"
description: "shpc-registry automated BioContainers addition for taranis"
config: {"url": "https://biocontainers.pro/tools/taranis", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for taranis", "latest": {"2.0.1--hdfd78af_0": "sha256:f46b5422c3046ae31f3096d2d0877b8e6f4ecf6dac324c127dac030ea945caf8"}, "tags": {"2.0.1--hdfd78af_0": "sha256:f46b5422c3046ae31f3096d2d0877b8e6f4ecf6dac324c127dac030ea945caf8"}, "docker": "quay.io/biocontainers/taranis", "aliases": {"Dockerfile": "/usr/local/bin/Dockerfile", "allele_calling.py": "/usr/local/bin/allele_calling.py", "analyze_schema.py": "/usr/local/bin/analyze_schema.py", "create_schema.py": "/usr/local/bin/create_schema.py", "distance_matrix.py": "/usr/local/bin/distance_matrix.py", "environment.yml": "/usr/local/bin/environment.yml", "logging_config.ini": "/usr/local/bin/logging_config.ini", "reference_alleles.py": "/usr/local/bin/reference_alleles.py", "taranis.py": "/usr/local/bin/taranis.py", "taranis_configuration.py": "/usr/local/bin/taranis_configuration.py", "2to3-3.7": "/usr/local/bin/2to3-3.7", "CA.pm": "/usr/local/bin/CA.pm", "LICENSE": "/usr/local/bin/LICENSE", "SOAPsh.pl": "/usr/local/bin/SOAPsh.pl", "accn-at-a-time": "/usr/local/bin/accn-at-a-time", "ace.pl": "/usr/local/bin/ace.pl", "acyclic": "/usr/local/bin/acyclic", "alimask": "/usr/local/bin/alimask", "amino-acid-composition": "/usr/local/bin/amino-acid-composition", "annotate": "/usr/local/bin/annotate"}}
---

This module is a singularity container wrapper for quay.io/biocontainers/taranis.
shpc-registry automated BioContainers addition for taranis
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/taranis
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/taranis:2.0.1--hdfd78af_0
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/taranis/2.0.1--hdfd78af_0
$ module help quay.io/biocontainers/taranis/2.0.1--hdfd78af_0
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### taranis-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### taranis-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### taranis-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### taranis-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### taranis-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### taranis-inspect-deffile:

```bash
$ singularity inspect -d <container>
```


#### Dockerfile

```bash
$ singularity exec <container> /usr/local/bin/Dockerfile
$ podman run --it --rm --entrypoint /usr/local/bin/Dockerfile   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/Dockerfile   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### allele_calling.py

```bash
$ singularity exec <container> /usr/local/bin/allele_calling.py
$ podman run --it --rm --entrypoint /usr/local/bin/allele_calling.py   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/allele_calling.py   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### analyze_schema.py

```bash
$ singularity exec <container> /usr/local/bin/analyze_schema.py
$ podman run --it --rm --entrypoint /usr/local/bin/analyze_schema.py   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/analyze_schema.py   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### create_schema.py

```bash
$ singularity exec <container> /usr/local/bin/create_schema.py
$ podman run --it --rm --entrypoint /usr/local/bin/create_schema.py   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/create_schema.py   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### distance_matrix.py

```bash
$ singularity exec <container> /usr/local/bin/distance_matrix.py
$ podman run --it --rm --entrypoint /usr/local/bin/distance_matrix.py   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/distance_matrix.py   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### environment.yml

```bash
$ singularity exec <container> /usr/local/bin/environment.yml
$ podman run --it --rm --entrypoint /usr/local/bin/environment.yml   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/environment.yml   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### logging_config.ini

```bash
$ singularity exec <container> /usr/local/bin/logging_config.ini
$ podman run --it --rm --entrypoint /usr/local/bin/logging_config.ini   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/logging_config.ini   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### reference_alleles.py

```bash
$ singularity exec <container> /usr/local/bin/reference_alleles.py
$ podman run --it --rm --entrypoint /usr/local/bin/reference_alleles.py   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/reference_alleles.py   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### taranis.py

```bash
$ singularity exec <container> /usr/local/bin/taranis.py
$ podman run --it --rm --entrypoint /usr/local/bin/taranis.py   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/taranis.py   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### taranis_configuration.py

```bash
$ singularity exec <container> /usr/local/bin/taranis_configuration.py
$ podman run --it --rm --entrypoint /usr/local/bin/taranis_configuration.py   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/taranis_configuration.py   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### 2to3-3.7

```bash
$ singularity exec <container> /usr/local/bin/2to3-3.7
$ podman run --it --rm --entrypoint /usr/local/bin/2to3-3.7   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/2to3-3.7   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### CA.pm

```bash
$ singularity exec <container> /usr/local/bin/CA.pm
$ podman run --it --rm --entrypoint /usr/local/bin/CA.pm   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/CA.pm   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### LICENSE

```bash
$ singularity exec <container> /usr/local/bin/LICENSE
$ podman run --it --rm --entrypoint /usr/local/bin/LICENSE   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/LICENSE   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### SOAPsh.pl

```bash
$ singularity exec <container> /usr/local/bin/SOAPsh.pl
$ podman run --it --rm --entrypoint /usr/local/bin/SOAPsh.pl   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/SOAPsh.pl   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### accn-at-a-time

```bash
$ singularity exec <container> /usr/local/bin/accn-at-a-time
$ podman run --it --rm --entrypoint /usr/local/bin/accn-at-a-time   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/accn-at-a-time   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### ace.pl

```bash
$ singularity exec <container> /usr/local/bin/ace.pl
$ podman run --it --rm --entrypoint /usr/local/bin/ace.pl   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/ace.pl   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### acyclic

```bash
$ singularity exec <container> /usr/local/bin/acyclic
$ podman run --it --rm --entrypoint /usr/local/bin/acyclic   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/acyclic   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### alimask

```bash
$ singularity exec <container> /usr/local/bin/alimask
$ podman run --it --rm --entrypoint /usr/local/bin/alimask   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/alimask   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### amino-acid-composition

```bash
$ singularity exec <container> /usr/local/bin/amino-acid-composition
$ podman run --it --rm --entrypoint /usr/local/bin/amino-acid-composition   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/amino-acid-composition   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### annotate

```bash
$ singularity exec <container> /usr/local/bin/annotate
$ podman run --it --rm --entrypoint /usr/local/bin/annotate   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/annotate   -v ${PWD} -w ${PWD} <container> -c " $@"
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
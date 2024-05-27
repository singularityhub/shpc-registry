---
layout: container
name:  "quay.io/biocontainers/bioconductor-cetf"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/bioconductor-cetf/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/bioconductor-cetf/container.yaml"
updated_at: "2024-05-27 03:07:30.153372"
latest: "1.14.0--r43hf17093f_0"
container_url: "https://biocontainers.pro/tools/bioconductor-cetf"
aliases:
 - "Cytoscape"
 - "cytoscape.sh"
 - "gen_vmoptions.sh"
 - "jpackage"
 - "curve_keygen"
 - "cups-config"
 - "ippeveprinter"
 - "ipptool"
 - "glpsol"
 - "f2py3.10"
versions:
 - "1.6.0--r41hc247a5b_2"
 - "1.9.0--r42hc247a5b_0"
 - "1.12.0--r43hf17093f_0"
 - "1.14.0--r43hf17093f_0"
description: "shpc-registry automated BioContainers addition for bioconductor-cetf"
config: {"url": "https://biocontainers.pro/tools/bioconductor-cetf", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for bioconductor-cetf", "latest": {"1.14.0--r43hf17093f_0": "sha256:e45482863cd703b3801b211069d7ed137f9cb73defc96a5a87b19725604c1681"}, "tags": {"1.6.0--r41hc247a5b_2": "sha256:9c55d9f8096bc6564eff18b22e8cb05a11ddc23e9213f253f4f47e30baf9ee31", "1.9.0--r42hc247a5b_0": "sha256:fd6fb7714ef8e375da5a9d95ed07c882448f558d8ef4582805147db024fe610b", "1.12.0--r43hf17093f_0": "sha256:4a650e3c5fb27f24b775b2c3c075cd5fb02ff093e7dbfa24cacc9cfa112b5324", "1.14.0--r43hf17093f_0": "sha256:e45482863cd703b3801b211069d7ed137f9cb73defc96a5a87b19725604c1681"}, "docker": "quay.io/biocontainers/bioconductor-cetf", "aliases": {"Cytoscape": "/usr/local/bin/Cytoscape", "cytoscape.sh": "/usr/local/bin/cytoscape.sh", "gen_vmoptions.sh": "/usr/local/bin/gen_vmoptions.sh", "jpackage": "/usr/local/bin/jpackage", "curve_keygen": "/usr/local/bin/curve_keygen", "cups-config": "/usr/local/bin/cups-config", "ippeveprinter": "/usr/local/bin/ippeveprinter", "ipptool": "/usr/local/bin/ipptool", "glpsol": "/usr/local/bin/glpsol", "f2py3.10": "/usr/local/bin/f2py3.10"}}
---

This module is a singularity container wrapper for quay.io/biocontainers/bioconductor-cetf.
shpc-registry automated BioContainers addition for bioconductor-cetf
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/bioconductor-cetf
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/bioconductor-cetf:1.14.0--r43hf17093f_0
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/bioconductor-cetf/1.14.0--r43hf17093f_0
$ module help quay.io/biocontainers/bioconductor-cetf/1.14.0--r43hf17093f_0
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### bioconductor-cetf-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### bioconductor-cetf-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### bioconductor-cetf-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### bioconductor-cetf-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### bioconductor-cetf-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### bioconductor-cetf-inspect-deffile:

```bash
$ singularity inspect -d <container>
```


#### Cytoscape

```bash
$ singularity exec <container> /usr/local/bin/Cytoscape
$ podman run --it --rm --entrypoint /usr/local/bin/Cytoscape   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/Cytoscape   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### cytoscape.sh

```bash
$ singularity exec <container> /usr/local/bin/cytoscape.sh
$ podman run --it --rm --entrypoint /usr/local/bin/cytoscape.sh   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/cytoscape.sh   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### gen_vmoptions.sh

```bash
$ singularity exec <container> /usr/local/bin/gen_vmoptions.sh
$ podman run --it --rm --entrypoint /usr/local/bin/gen_vmoptions.sh   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/gen_vmoptions.sh   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### jpackage

```bash
$ singularity exec <container> /usr/local/bin/jpackage
$ podman run --it --rm --entrypoint /usr/local/bin/jpackage   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/jpackage   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### curve_keygen

```bash
$ singularity exec <container> /usr/local/bin/curve_keygen
$ podman run --it --rm --entrypoint /usr/local/bin/curve_keygen   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/curve_keygen   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### cups-config

```bash
$ singularity exec <container> /usr/local/bin/cups-config
$ podman run --it --rm --entrypoint /usr/local/bin/cups-config   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/cups-config   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### ippeveprinter

```bash
$ singularity exec <container> /usr/local/bin/ippeveprinter
$ podman run --it --rm --entrypoint /usr/local/bin/ippeveprinter   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/ippeveprinter   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### ipptool

```bash
$ singularity exec <container> /usr/local/bin/ipptool
$ podman run --it --rm --entrypoint /usr/local/bin/ipptool   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/ipptool   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### glpsol

```bash
$ singularity exec <container> /usr/local/bin/glpsol
$ podman run --it --rm --entrypoint /usr/local/bin/glpsol   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/glpsol   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### f2py3.10

```bash
$ singularity exec <container> /usr/local/bin/f2py3.10
$ podman run --it --rm --entrypoint /usr/local/bin/f2py3.10   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/f2py3.10   -v ${PWD} -w ${PWD} <container> -c " $@"
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
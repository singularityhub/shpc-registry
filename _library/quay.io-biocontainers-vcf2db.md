---
layout: container
name:  "quay.io/biocontainers/vcf2db"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/vcf2db/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/vcf2db/container.yaml"
updated_at: "2025-02-13 03:14:25.309617"
latest: "2020.02.24--pl5321hdfd78af_3"
container_url: "https://biocontainers.pro/tools/vcf2db"
aliases:
 - "peddy"
 - "toolshed"
 - "vcf2db.py"
 - "cyvcf2"
 - "coloredlogs"
 - "humanfriendly"
 - "f2py3.8"
 - "htsfile"
 - "bgzip"
 - "tabix"
 - "2to3-3.8"
 - "idle3.8"
 - "pydoc3.8"
versions:
 - "2020.02.24--hdfd78af_1"
 - "2020.02.24--pl5321hdfd78af_3"
description: "shpc-registry automated BioContainers addition for vcf2db"
config: {"url": "https://biocontainers.pro/tools/vcf2db", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for vcf2db", "latest": {"2020.02.24--pl5321hdfd78af_3": "sha256:a54d14aee0eb6f7c2733012cec5a52fbfa1d91385cc93e17c8bfc622e4694e39"}, "tags": {"2020.02.24--hdfd78af_1": "sha256:8cdcd3a78130e2e9975e034983d9973b1d153e4f1a5f2cf300918f8a41f5db11", "2020.02.24--pl5321hdfd78af_3": "sha256:a54d14aee0eb6f7c2733012cec5a52fbfa1d91385cc93e17c8bfc622e4694e39"}, "docker": "quay.io/biocontainers/vcf2db", "aliases": {"peddy": "/usr/local/bin/peddy", "toolshed": "/usr/local/bin/toolshed", "vcf2db.py": "/usr/local/bin/vcf2db.py", "cyvcf2": "/usr/local/bin/cyvcf2", "coloredlogs": "/usr/local/bin/coloredlogs", "humanfriendly": "/usr/local/bin/humanfriendly", "f2py3.8": "/usr/local/bin/f2py3.8", "htsfile": "/usr/local/bin/htsfile", "bgzip": "/usr/local/bin/bgzip", "tabix": "/usr/local/bin/tabix", "2to3-3.8": "/usr/local/bin/2to3-3.8", "idle3.8": "/usr/local/bin/idle3.8", "pydoc3.8": "/usr/local/bin/pydoc3.8"}}
---

This module is a singularity container wrapper for quay.io/biocontainers/vcf2db.
shpc-registry automated BioContainers addition for vcf2db
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/vcf2db
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/vcf2db:2020.02.24--pl5321hdfd78af_3
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/vcf2db/2020.02.24--pl5321hdfd78af_3
$ module help quay.io/biocontainers/vcf2db/2020.02.24--pl5321hdfd78af_3
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### vcf2db-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### vcf2db-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### vcf2db-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### vcf2db-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### vcf2db-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### vcf2db-inspect-deffile:

```bash
$ singularity inspect -d <container>
```


#### peddy

```bash
$ singularity exec <container> /usr/local/bin/peddy
$ podman run --it --rm --entrypoint /usr/local/bin/peddy   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/peddy   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### toolshed

```bash
$ singularity exec <container> /usr/local/bin/toolshed
$ podman run --it --rm --entrypoint /usr/local/bin/toolshed   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/toolshed   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### vcf2db.py

```bash
$ singularity exec <container> /usr/local/bin/vcf2db.py
$ podman run --it --rm --entrypoint /usr/local/bin/vcf2db.py   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/vcf2db.py   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### cyvcf2

```bash
$ singularity exec <container> /usr/local/bin/cyvcf2
$ podman run --it --rm --entrypoint /usr/local/bin/cyvcf2   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/cyvcf2   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### coloredlogs

```bash
$ singularity exec <container> /usr/local/bin/coloredlogs
$ podman run --it --rm --entrypoint /usr/local/bin/coloredlogs   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/coloredlogs   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### humanfriendly

```bash
$ singularity exec <container> /usr/local/bin/humanfriendly
$ podman run --it --rm --entrypoint /usr/local/bin/humanfriendly   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/humanfriendly   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### f2py3.8

```bash
$ singularity exec <container> /usr/local/bin/f2py3.8
$ podman run --it --rm --entrypoint /usr/local/bin/f2py3.8   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/f2py3.8   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### htsfile

```bash
$ singularity exec <container> /usr/local/bin/htsfile
$ podman run --it --rm --entrypoint /usr/local/bin/htsfile   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/htsfile   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### bgzip

```bash
$ singularity exec <container> /usr/local/bin/bgzip
$ podman run --it --rm --entrypoint /usr/local/bin/bgzip   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/bgzip   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### tabix

```bash
$ singularity exec <container> /usr/local/bin/tabix
$ podman run --it --rm --entrypoint /usr/local/bin/tabix   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/tabix   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### 2to3-3.8

```bash
$ singularity exec <container> /usr/local/bin/2to3-3.8
$ podman run --it --rm --entrypoint /usr/local/bin/2to3-3.8   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/2to3-3.8   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### idle3.8

```bash
$ singularity exec <container> /usr/local/bin/idle3.8
$ podman run --it --rm --entrypoint /usr/local/bin/idle3.8   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/idle3.8   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### pydoc3.8

```bash
$ singularity exec <container> /usr/local/bin/pydoc3.8
$ podman run --it --rm --entrypoint /usr/local/bin/pydoc3.8   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/pydoc3.8   -v ${PWD} -w ${PWD} <container> -c " $@"
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
---
layout: container
name:  "quay.io/biocontainers/mafft"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/mafft/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/mafft/container.yaml"
updated_at: "2023-06-23 03:02:27.741856"
latest: "7.520--h031d066_2"
container_url: "https://biocontainers.pro/tools/mafft"
aliases:
 - "mafft"
 - "mafft-distance"
 - "mafft-einsi"
 - "mafft-fftns"
 - "mafft-fftnsi"
 - "mafft-ginsi"
 - "mafft-homologs.rb"
 - "mafft-linsi"
 - "mafft-nwns"
 - "mafft-nwnsi"
 - "mafft-profile"
 - "mafft-qinsi"
 - "mafft-sparsecore.rb"
 - "mafft-xinsi"
 - "einsi"
 - "fftns"
 - "fftnsi"
 - "ginsi"
 - "linsi"
 - "nwns"
 - "nwnsi"
versions:
 - "7.508--hec16e2b_0"
 - "7.515--hec16e2b_0"
 - "7.520--hec16e2b_0-test-bot-free-upload"
 - "7.520--h031d066_2"
description: "shpc-registry automated BioContainers addition for mafft"
config: {"url": "https://biocontainers.pro/tools/mafft", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for mafft", "latest": {"7.520--h031d066_2": "sha256:ef404acfcb00dfdf55dceaaac9040bddd6ab25d99ef35cfe4963c4879018ed65"}, "tags": {"7.508--hec16e2b_0": "sha256:954a2b33ac01adde300de1867582230db0eb8afb41801cc2c51d18ca29dff12d", "7.515--hec16e2b_0": "sha256:1a5cbc04aecd5108e05ae1bd748a7abaa3520afa6b07115aed5d79af8346ff72", "7.520--hec16e2b_0-test-bot-free-upload": "sha256:c4560d6b4fa2a21142689352720cb4bfa726dbc0a2080abd53044270c131e43d", "7.520--h031d066_2": "sha256:ef404acfcb00dfdf55dceaaac9040bddd6ab25d99ef35cfe4963c4879018ed65"}, "docker": "quay.io/biocontainers/mafft", "aliases": {"mafft": "/usr/local/bin/mafft", "mafft-distance": "/usr/local/bin/mafft-distance", "mafft-einsi": "/usr/local/bin/mafft-einsi", "mafft-fftns": "/usr/local/bin/mafft-fftns", "mafft-fftnsi": "/usr/local/bin/mafft-fftnsi", "mafft-ginsi": "/usr/local/bin/mafft-ginsi", "mafft-homologs.rb": "/usr/local/bin/mafft-homologs.rb", "mafft-linsi": "/usr/local/bin/mafft-linsi", "mafft-nwns": "/usr/local/bin/mafft-nwns", "mafft-nwnsi": "/usr/local/bin/mafft-nwnsi", "mafft-profile": "/usr/local/bin/mafft-profile", "mafft-qinsi": "/usr/local/bin/mafft-qinsi", "mafft-sparsecore.rb": "/usr/local/bin/mafft-sparsecore.rb", "mafft-xinsi": "/usr/local/bin/mafft-xinsi", "einsi": "/usr/local/bin/einsi", "fftns": "/usr/local/bin/fftns", "fftnsi": "/usr/local/bin/fftnsi", "ginsi": "/usr/local/bin/ginsi", "linsi": "/usr/local/bin/linsi", "nwns": "/usr/local/bin/nwns", "nwnsi": "/usr/local/bin/nwnsi"}}
---

This module is a singularity container wrapper for quay.io/biocontainers/mafft.
shpc-registry automated BioContainers addition for mafft
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/mafft
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/mafft:7.520--h031d066_2
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/mafft/7.520--h031d066_2
$ module help quay.io/biocontainers/mafft/7.520--h031d066_2
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### mafft-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### mafft-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### mafft-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### mafft-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### mafft-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### mafft-inspect-deffile:

```bash
$ singularity inspect -d <container>
```


#### mafft

```bash
$ singularity exec <container> /usr/local/bin/mafft
$ podman run --it --rm --entrypoint /usr/local/bin/mafft   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/mafft   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### mafft-distance

```bash
$ singularity exec <container> /usr/local/bin/mafft-distance
$ podman run --it --rm --entrypoint /usr/local/bin/mafft-distance   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/mafft-distance   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### mafft-einsi

```bash
$ singularity exec <container> /usr/local/bin/mafft-einsi
$ podman run --it --rm --entrypoint /usr/local/bin/mafft-einsi   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/mafft-einsi   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### mafft-fftns

```bash
$ singularity exec <container> /usr/local/bin/mafft-fftns
$ podman run --it --rm --entrypoint /usr/local/bin/mafft-fftns   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/mafft-fftns   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### mafft-fftnsi

```bash
$ singularity exec <container> /usr/local/bin/mafft-fftnsi
$ podman run --it --rm --entrypoint /usr/local/bin/mafft-fftnsi   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/mafft-fftnsi   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### mafft-ginsi

```bash
$ singularity exec <container> /usr/local/bin/mafft-ginsi
$ podman run --it --rm --entrypoint /usr/local/bin/mafft-ginsi   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/mafft-ginsi   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### mafft-homologs.rb

```bash
$ singularity exec <container> /usr/local/bin/mafft-homologs.rb
$ podman run --it --rm --entrypoint /usr/local/bin/mafft-homologs.rb   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/mafft-homologs.rb   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### mafft-linsi

```bash
$ singularity exec <container> /usr/local/bin/mafft-linsi
$ podman run --it --rm --entrypoint /usr/local/bin/mafft-linsi   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/mafft-linsi   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### mafft-nwns

```bash
$ singularity exec <container> /usr/local/bin/mafft-nwns
$ podman run --it --rm --entrypoint /usr/local/bin/mafft-nwns   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/mafft-nwns   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### mafft-nwnsi

```bash
$ singularity exec <container> /usr/local/bin/mafft-nwnsi
$ podman run --it --rm --entrypoint /usr/local/bin/mafft-nwnsi   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/mafft-nwnsi   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### mafft-profile

```bash
$ singularity exec <container> /usr/local/bin/mafft-profile
$ podman run --it --rm --entrypoint /usr/local/bin/mafft-profile   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/mafft-profile   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### mafft-qinsi

```bash
$ singularity exec <container> /usr/local/bin/mafft-qinsi
$ podman run --it --rm --entrypoint /usr/local/bin/mafft-qinsi   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/mafft-qinsi   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### mafft-sparsecore.rb

```bash
$ singularity exec <container> /usr/local/bin/mafft-sparsecore.rb
$ podman run --it --rm --entrypoint /usr/local/bin/mafft-sparsecore.rb   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/mafft-sparsecore.rb   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### mafft-xinsi

```bash
$ singularity exec <container> /usr/local/bin/mafft-xinsi
$ podman run --it --rm --entrypoint /usr/local/bin/mafft-xinsi   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/mafft-xinsi   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### einsi

```bash
$ singularity exec <container> /usr/local/bin/einsi
$ podman run --it --rm --entrypoint /usr/local/bin/einsi   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/einsi   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### fftns

```bash
$ singularity exec <container> /usr/local/bin/fftns
$ podman run --it --rm --entrypoint /usr/local/bin/fftns   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/fftns   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### fftnsi

```bash
$ singularity exec <container> /usr/local/bin/fftnsi
$ podman run --it --rm --entrypoint /usr/local/bin/fftnsi   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/fftnsi   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### ginsi

```bash
$ singularity exec <container> /usr/local/bin/ginsi
$ podman run --it --rm --entrypoint /usr/local/bin/ginsi   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/ginsi   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### linsi

```bash
$ singularity exec <container> /usr/local/bin/linsi
$ podman run --it --rm --entrypoint /usr/local/bin/linsi   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/linsi   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### nwns

```bash
$ singularity exec <container> /usr/local/bin/nwns
$ podman run --it --rm --entrypoint /usr/local/bin/nwns   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/nwns   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### nwnsi

```bash
$ singularity exec <container> /usr/local/bin/nwnsi
$ podman run --it --rm --entrypoint /usr/local/bin/nwnsi   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/nwnsi   -v ${PWD} -w ${PWD} <container> -c " $@"
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
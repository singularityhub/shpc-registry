---
layout: container
name:  "quay.io/biocontainers/perl-ms"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/perl-ms/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/perl-ms/container.yaml"
updated_at: "2024-05-31 03:06:46.342211"
latest: "0.207003--pl5321hdfd78af_0"
container_url: "https://biocontainers.pro/tools/perl-ms"
aliases:
 - "bgzip.pl"
 - "cv2storable.pl"
 - "index_mzml"
 - "index_pepxml"
 - "unimod2storable.pl"
 - "perl5.32.1"
 - "streamzip"
versions:
 - "0.207002--pl5321hdfd78af_0"
 - "0.207003--pl5321hdfd78af_0"
description: "shpc-registry automated BioContainers addition for perl-ms"
config: {"url": "https://biocontainers.pro/tools/perl-ms", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for perl-ms", "latest": {"0.207003--pl5321hdfd78af_0": "sha256:e230ba7a8f992e668e6ab0542909028aa23545b426c125d247e863ec42ec144b"}, "tags": {"0.207002--pl5321hdfd78af_0": "sha256:0aca2b426acdf483003e49fa4da0bd99915b283c6a9ad580e62bfb7a0c369d59", "0.207003--pl5321hdfd78af_0": "sha256:e230ba7a8f992e668e6ab0542909028aa23545b426c125d247e863ec42ec144b"}, "docker": "quay.io/biocontainers/perl-ms", "aliases": {"bgzip.pl": "/usr/local/bin/bgzip.pl", "cv2storable.pl": "/usr/local/bin/cv2storable.pl", "index_mzml": "/usr/local/bin/index_mzml", "index_pepxml": "/usr/local/bin/index_pepxml", "unimod2storable.pl": "/usr/local/bin/unimod2storable.pl", "perl5.32.1": "/usr/local/bin/perl5.32.1", "streamzip": "/usr/local/bin/streamzip"}}
---

This module is a singularity container wrapper for quay.io/biocontainers/perl-ms.
shpc-registry automated BioContainers addition for perl-ms
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/perl-ms
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/perl-ms:0.207003--pl5321hdfd78af_0
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/perl-ms/0.207003--pl5321hdfd78af_0
$ module help quay.io/biocontainers/perl-ms/0.207003--pl5321hdfd78af_0
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### perl-ms-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### perl-ms-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### perl-ms-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### perl-ms-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### perl-ms-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### perl-ms-inspect-deffile:

```bash
$ singularity inspect -d <container>
```


#### bgzip.pl

```bash
$ singularity exec <container> /usr/local/bin/bgzip.pl
$ podman run --it --rm --entrypoint /usr/local/bin/bgzip.pl   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/bgzip.pl   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### cv2storable.pl

```bash
$ singularity exec <container> /usr/local/bin/cv2storable.pl
$ podman run --it --rm --entrypoint /usr/local/bin/cv2storable.pl   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/cv2storable.pl   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### index_mzml

```bash
$ singularity exec <container> /usr/local/bin/index_mzml
$ podman run --it --rm --entrypoint /usr/local/bin/index_mzml   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/index_mzml   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### index_pepxml

```bash
$ singularity exec <container> /usr/local/bin/index_pepxml
$ podman run --it --rm --entrypoint /usr/local/bin/index_pepxml   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/index_pepxml   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### unimod2storable.pl

```bash
$ singularity exec <container> /usr/local/bin/unimod2storable.pl
$ podman run --it --rm --entrypoint /usr/local/bin/unimod2storable.pl   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/unimod2storable.pl   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### perl5.32.1

```bash
$ singularity exec <container> /usr/local/bin/perl5.32.1
$ podman run --it --rm --entrypoint /usr/local/bin/perl5.32.1   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/perl5.32.1   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### streamzip

```bash
$ singularity exec <container> /usr/local/bin/streamzip
$ podman run --it --rm --entrypoint /usr/local/bin/streamzip   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/streamzip   -v ${PWD} -w ${PWD} <container> -c " $@"
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
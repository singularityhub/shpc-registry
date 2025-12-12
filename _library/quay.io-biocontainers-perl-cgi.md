---
layout: container
name:  "quay.io/biocontainers/perl-cgi"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/perl-cgi/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/perl-cgi/container.yaml"
updated_at: "2025-12-12 03:49:22.334574"
latest: "4.71--pl5321h7b50bb2_0"
container_url: "https://biocontainers.pro/tools/perl-cgi"
aliases:
 - "perl5.32.1"
 - "streamzip"
versions:
 - "4.54--pl5321hec16e2b_1"
 - "4.55--pl5321hec16e2b_0"
 - "4.56--pl5321hec16e2b_0"
 - "4.56--pl5321h031d066_1"
 - "4.56--pl5321h7b50bb2_2"
 - "4.67--pl5321h7b50bb2_0"
 - "4.67--pl5321h7b50bb2_1"
 - "4.67--pl5321h7b50bb2_2"
 - "4.70--pl5321h7b50bb2_0"
 - "4.69--pl5321h7b50bb2_0"
 - "4.71--pl5321h7b50bb2_0"
description: "shpc-registry automated BioContainers addition for perl-cgi"
config: {"url": "https://biocontainers.pro/tools/perl-cgi", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for perl-cgi", "latest": {"4.71--pl5321h7b50bb2_0": "sha256:365604f30324acdbf2e9077efc49381093b6a628a37c20ea1c3672806ab542a3"}, "tags": {"4.54--pl5321hec16e2b_1": "sha256:447db43794c1be154b87efacf3fd69c5aec24cd1173f2cd20059582e038ef192", "4.55--pl5321hec16e2b_0": "sha256:f693ea25a5f6473faf11e8e3d9f1d982a2d1d2732ce6309d20ac13f5a69dd549", "4.56--pl5321hec16e2b_0": "sha256:15126906cb3d0c3e39a99e79597ff9aa9feb3e78d70a8e6d6c2299dcd406c241", "4.56--pl5321h031d066_1": "sha256:352193a3ae081eeaedda923eac0f399711fcdd9679122c6bbf2b43a695a5f6ba", "4.56--pl5321h7b50bb2_2": "sha256:9cabbdd3415e505873d158e080a6af05e13a224d54c2b4262a1827e627dbf824", "4.67--pl5321h7b50bb2_0": "sha256:d4c76f10d9a2c79cb184d0f9b601586a9690107f6f82dbd177fbe2190edb9801", "4.67--pl5321h7b50bb2_1": "sha256:d85925be057da9f32f99f911989acc92602daf0b5ea8df5d8936cd948a8be2cb", "4.67--pl5321h7b50bb2_2": "sha256:c092724d48bab26707e08796fda5337c39195c5a1d01c91510e0a35b0219cb0f", "4.70--pl5321h7b50bb2_0": "sha256:d36e7da471101a0f9136c55f6bbf496c751cc369d5a0ba07c8290108358e147b", "4.69--pl5321h7b50bb2_0": "sha256:5595914e8388fba2121bf6d93f09b2342c502da9b5d87bbdbba957eb1acd3531", "4.71--pl5321h7b50bb2_0": "sha256:365604f30324acdbf2e9077efc49381093b6a628a37c20ea1c3672806ab542a3"}, "docker": "quay.io/biocontainers/perl-cgi", "aliases": {"perl5.32.1": "/usr/local/bin/perl5.32.1", "streamzip": "/usr/local/bin/streamzip"}}
---

This module is a singularity container wrapper for quay.io/biocontainers/perl-cgi.
shpc-registry automated BioContainers addition for perl-cgi
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/perl-cgi
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/perl-cgi:4.71--pl5321h7b50bb2_0
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/perl-cgi/4.71--pl5321h7b50bb2_0
$ module help quay.io/biocontainers/perl-cgi/4.71--pl5321h7b50bb2_0
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### perl-cgi-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### perl-cgi-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### perl-cgi-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### perl-cgi-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### perl-cgi-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### perl-cgi-inspect-deffile:

```bash
$ singularity inspect -d <container>
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
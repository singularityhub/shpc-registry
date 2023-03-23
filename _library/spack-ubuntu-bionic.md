---
layout: container
name:  "spack/ubuntu-bionic"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/spack/ubuntu-bionic/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/spack/ubuntu-bionic/container.yaml"
updated_at: "2023-03-23 03:51:07.652111"
latest: "v0.19.1"
container_url: "https://hub.docker.com/r/spack/ubuntu-bionic"
aliases:
 - "sbang"
 - "spack"
 - "spack-python"
versions:
 - "0.16.1"
 - "0.16.2"
 - "0.16.3"
 - "latest"
 - "0.16"
 - "prerelease"
 - "v0.17.2"
 - "v0.18.0"
 - "v0.18.1"
 - "v0.17.3"
 - "v0.19.0"
 - "v0.19.1"
description: "Ubuntu 18.04 with Spack preinstalled."
config: {"docker": "spack/ubuntu-bionic", "url": "https://hub.docker.com/r/spack/ubuntu-bionic", "maintainer": "@vsoch", "description": "Ubuntu 18.04 with Spack preinstalled.", "latest": {"v0.19.1": "sha256:ba47c03551762bbd0c46758d576039af41dfb5e27f2619ab31cd4c382c17f7df"}, "tags": {"0.16.1": "sha256:8261977ff63fe420446c349f0e3bd4e09a6417ebb1008ab472861041f1edd11b", "0.16.2": "sha256:698899684998df4a49f02bce1cffca9aa59644477f94b1909fc26b2adf4c4be4", "0.16.3": "sha256:fd9bfae1b8133bfb1c8636434f5ec24b2deae94e6b21d533cf6ee6df19af0772", "latest": "sha256:2b0523e8ca9d25088511d737013e17e95d8ca2589a94086a5e5906722c2e8231", "0.16": "sha256:5c6e3f016333b48bc85fa3e42634bb77d8af318c28c69b575e279cd875a93fe0", "prerelease": "sha256:e8565c944612471f06df71364e2ae390a9483837d116b208e7b476086b05ba4a", "v0.17.2": "sha256:29730dee9527826dfb3de157f46daefa68cedb611b2b393d06f4cb074c3223c5", "v0.18.0": "sha256:585efe3455c4ecd1781f7cb711e5b072a3fbc18acc200550d9264f1124de51f1", "v0.18.1": "sha256:a08a59a72667ff9e2f66c9fdfe26f1aa856ab9c91e98e798fc1be91a51c9d677", "v0.17.3": "sha256:4f81a2008abd021dc128481caa31f607a0a659e08756886f79296b6dc3f0bf09", "v0.19.0": "sha256:4fe221bae91f1efa64ad10bb158ea2317781a64ecc6877cb61e80bdab15957de", "v0.19.1": "sha256:ba47c03551762bbd0c46758d576039af41dfb5e27f2619ab31cd4c382c17f7df"}, "aliases": {"sbang": "/opt/spack/bin/sbang", "spack": "/opt/spack/bin/spack", "spack-python": "/opt/spack/bin/spack-python"}}
---

This module is a singularity container wrapper for spack/ubuntu-bionic.
Ubuntu 18.04 with Spack preinstalled.
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install spack/ubuntu-bionic
```

Or a specific version:

```bash
$ shpc install spack/ubuntu-bionic:v0.19.1
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load spack/ubuntu-bionic/v0.19.1
$ module help spack/ubuntu-bionic/v0.19.1
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### ubuntu-bionic-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### ubuntu-bionic-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### ubuntu-bionic-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### ubuntu-bionic-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### ubuntu-bionic-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### ubuntu-bionic-inspect-deffile:

```bash
$ singularity inspect -d <container>
```


#### sbang

```bash
$ singularity exec <container> /opt/spack/bin/sbang
$ podman run --it --rm --entrypoint /opt/spack/bin/sbang   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /opt/spack/bin/sbang   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### spack

```bash
$ singularity exec <container> /opt/spack/bin/spack
$ podman run --it --rm --entrypoint /opt/spack/bin/spack   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /opt/spack/bin/spack   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### spack-python

```bash
$ singularity exec <container> /opt/spack/bin/spack-python
$ podman run --it --rm --entrypoint /opt/spack/bin/spack-python   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /opt/spack/bin/spack-python   -v ${PWD} -w ${PWD} <container> -c " $@"
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
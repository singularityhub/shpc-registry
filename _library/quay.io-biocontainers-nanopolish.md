---
layout: container
name:  "quay.io/biocontainers/nanopolish"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/nanopolish/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/nanopolish/container.yaml"
updated_at: "2023-11-03 02:31:59.421971"
latest: "0.14.0--h893af9b_2"
container_url: "https://biocontainers.pro/tools/nanopolish"
aliases:
 - "ccmake"
 - "cmake"
 - "cpack"
 - "ctest"
 - "ed2k-link"
 - "gost-hash"
 - "has160-hash"
 - "magnet-link"
 - "nanopolish"
 - "nanopolish_makerange.py"
 - "nanopolish_merge.py"
 - "rhash"
 - "sfv-hash"
 - "tiger-hash"
 - "tth-hash"
 - "whirlpool-hash"
 - "enhancer.py"
 - "explode.py"
 - "gifmaker.py"
 - "painter.py"
 - "player.py"
 - "thresholder.py"
 - "viewer.py"
 - "pilconvert.py"
 - "pildriver.py"
 - "pilfile.py"
versions:
 - "0.9.2--py35_ncurses5.9_4"
 - "0.14.0--hb24e783_1"
 - "0.13.2--hd7c1219_10"
 - "0.12.5--ha077697_2"
 - "0.11.3--h705302d_0"
 - "0.10.2--h78a5b34_0"
 - "0.14.0--h893af9b_2"
description: "shpc-registry automated BioContainers addition for nanopolish"
config: {"url": "https://biocontainers.pro/tools/nanopolish", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for nanopolish", "latest": {"0.14.0--h893af9b_2": "sha256:fa64a8063edd47c35b39d4f26be5f66128fdc4afcf79cc4907fdd7f462d4df7e"}, "tags": {"0.9.2--py35_ncurses5.9_4": "sha256:7ebca1ed0119f110c84c02de5910f874d9345bb4087c6b0763c2102e09607310", "0.14.0--hb24e783_1": "sha256:216b64335890bef9ec3c58c0e8fb5036e8eaca054ab75755b0b95ba5f3965ea5", "0.13.2--hd7c1219_10": "sha256:bbf1732ee86df764e1a639ce59843da2e80543ee1716266c5e1210f366286821", "0.12.5--ha077697_2": "sha256:0c6a410d217e2f7f30bc8cdac1918ed636ec942bfe90a2ef4185eaf96c7cb31d", "0.11.3--h705302d_0": "sha256:298dce994cbe850cc2c6dcfb8f2e5aa3104a1b5a3bae6a452abea48867746d05", "0.10.2--h78a5b34_0": "sha256:14ab1f3c967a42b679e40ae3c80b814c83b3fdd9f92c2fbfa11ca9172c718913", "0.14.0--h893af9b_2": "sha256:fa64a8063edd47c35b39d4f26be5f66128fdc4afcf79cc4907fdd7f462d4df7e"}, "docker": "quay.io/biocontainers/nanopolish", "aliases": {"ccmake": "/usr/local/bin/ccmake", "cmake": "/usr/local/bin/cmake", "cpack": "/usr/local/bin/cpack", "ctest": "/usr/local/bin/ctest", "ed2k-link": "/usr/local/bin/ed2k-link", "gost-hash": "/usr/local/bin/gost-hash", "has160-hash": "/usr/local/bin/has160-hash", "magnet-link": "/usr/local/bin/magnet-link", "nanopolish": "/usr/local/bin/nanopolish", "nanopolish_makerange.py": "/usr/local/bin/nanopolish_makerange.py", "nanopolish_merge.py": "/usr/local/bin/nanopolish_merge.py", "rhash": "/usr/local/bin/rhash", "sfv-hash": "/usr/local/bin/sfv-hash", "tiger-hash": "/usr/local/bin/tiger-hash", "tth-hash": "/usr/local/bin/tth-hash", "whirlpool-hash": "/usr/local/bin/whirlpool-hash", "enhancer.py": "/usr/local/bin/enhancer.py", "explode.py": "/usr/local/bin/explode.py", "gifmaker.py": "/usr/local/bin/gifmaker.py", "painter.py": "/usr/local/bin/painter.py", "player.py": "/usr/local/bin/player.py", "thresholder.py": "/usr/local/bin/thresholder.py", "viewer.py": "/usr/local/bin/viewer.py", "pilconvert.py": "/usr/local/bin/pilconvert.py", "pildriver.py": "/usr/local/bin/pildriver.py", "pilfile.py": "/usr/local/bin/pilfile.py"}}
---

This module is a singularity container wrapper for quay.io/biocontainers/nanopolish.
shpc-registry automated BioContainers addition for nanopolish
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/nanopolish
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/nanopolish:0.14.0--h893af9b_2
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/nanopolish/0.14.0--h893af9b_2
$ module help quay.io/biocontainers/nanopolish/0.14.0--h893af9b_2
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### nanopolish-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### nanopolish-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### nanopolish-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### nanopolish-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### nanopolish-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### nanopolish-inspect-deffile:

```bash
$ singularity inspect -d <container>
```


#### ccmake

```bash
$ singularity exec <container> /usr/local/bin/ccmake
$ podman run --it --rm --entrypoint /usr/local/bin/ccmake   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/ccmake   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### cmake

```bash
$ singularity exec <container> /usr/local/bin/cmake
$ podman run --it --rm --entrypoint /usr/local/bin/cmake   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/cmake   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### cpack

```bash
$ singularity exec <container> /usr/local/bin/cpack
$ podman run --it --rm --entrypoint /usr/local/bin/cpack   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/cpack   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### ctest

```bash
$ singularity exec <container> /usr/local/bin/ctest
$ podman run --it --rm --entrypoint /usr/local/bin/ctest   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/ctest   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### ed2k-link

```bash
$ singularity exec <container> /usr/local/bin/ed2k-link
$ podman run --it --rm --entrypoint /usr/local/bin/ed2k-link   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/ed2k-link   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### gost-hash

```bash
$ singularity exec <container> /usr/local/bin/gost-hash
$ podman run --it --rm --entrypoint /usr/local/bin/gost-hash   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/gost-hash   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### has160-hash

```bash
$ singularity exec <container> /usr/local/bin/has160-hash
$ podman run --it --rm --entrypoint /usr/local/bin/has160-hash   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/has160-hash   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### magnet-link

```bash
$ singularity exec <container> /usr/local/bin/magnet-link
$ podman run --it --rm --entrypoint /usr/local/bin/magnet-link   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/magnet-link   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### nanopolish

```bash
$ singularity exec <container> /usr/local/bin/nanopolish
$ podman run --it --rm --entrypoint /usr/local/bin/nanopolish   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/nanopolish   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### nanopolish_makerange.py

```bash
$ singularity exec <container> /usr/local/bin/nanopolish_makerange.py
$ podman run --it --rm --entrypoint /usr/local/bin/nanopolish_makerange.py   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/nanopolish_makerange.py   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### nanopolish_merge.py

```bash
$ singularity exec <container> /usr/local/bin/nanopolish_merge.py
$ podman run --it --rm --entrypoint /usr/local/bin/nanopolish_merge.py   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/nanopolish_merge.py   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### rhash

```bash
$ singularity exec <container> /usr/local/bin/rhash
$ podman run --it --rm --entrypoint /usr/local/bin/rhash   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/rhash   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### sfv-hash

```bash
$ singularity exec <container> /usr/local/bin/sfv-hash
$ podman run --it --rm --entrypoint /usr/local/bin/sfv-hash   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/sfv-hash   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### tiger-hash

```bash
$ singularity exec <container> /usr/local/bin/tiger-hash
$ podman run --it --rm --entrypoint /usr/local/bin/tiger-hash   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/tiger-hash   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### tth-hash

```bash
$ singularity exec <container> /usr/local/bin/tth-hash
$ podman run --it --rm --entrypoint /usr/local/bin/tth-hash   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/tth-hash   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### whirlpool-hash

```bash
$ singularity exec <container> /usr/local/bin/whirlpool-hash
$ podman run --it --rm --entrypoint /usr/local/bin/whirlpool-hash   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/whirlpool-hash   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### enhancer.py

```bash
$ singularity exec <container> /usr/local/bin/enhancer.py
$ podman run --it --rm --entrypoint /usr/local/bin/enhancer.py   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/enhancer.py   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### explode.py

```bash
$ singularity exec <container> /usr/local/bin/explode.py
$ podman run --it --rm --entrypoint /usr/local/bin/explode.py   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/explode.py   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### gifmaker.py

```bash
$ singularity exec <container> /usr/local/bin/gifmaker.py
$ podman run --it --rm --entrypoint /usr/local/bin/gifmaker.py   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/gifmaker.py   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### painter.py

```bash
$ singularity exec <container> /usr/local/bin/painter.py
$ podman run --it --rm --entrypoint /usr/local/bin/painter.py   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/painter.py   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### player.py

```bash
$ singularity exec <container> /usr/local/bin/player.py
$ podman run --it --rm --entrypoint /usr/local/bin/player.py   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/player.py   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### thresholder.py

```bash
$ singularity exec <container> /usr/local/bin/thresholder.py
$ podman run --it --rm --entrypoint /usr/local/bin/thresholder.py   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/thresholder.py   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### viewer.py

```bash
$ singularity exec <container> /usr/local/bin/viewer.py
$ podman run --it --rm --entrypoint /usr/local/bin/viewer.py   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/viewer.py   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### pilconvert.py

```bash
$ singularity exec <container> /usr/local/bin/pilconvert.py
$ podman run --it --rm --entrypoint /usr/local/bin/pilconvert.py   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/pilconvert.py   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### pildriver.py

```bash
$ singularity exec <container> /usr/local/bin/pildriver.py
$ podman run --it --rm --entrypoint /usr/local/bin/pildriver.py   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/pildriver.py   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### pilfile.py

```bash
$ singularity exec <container> /usr/local/bin/pilfile.py
$ podman run --it --rm --entrypoint /usr/local/bin/pilfile.py   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/pilfile.py   -v ${PWD} -w ${PWD} <container> -c " $@"
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
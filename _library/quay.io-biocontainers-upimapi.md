---
layout: container
name:  "quay.io/biocontainers/upimapi"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/upimapi/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/upimapi/container.yaml"
updated_at: "2024-12-09 03:31:27.272784"
latest: "1.13.1--hdfd78af_0"
container_url: "https://biocontainers.pro/tools/upimapi"
aliases:
 - "firefox"
 - "geckodriver"
 - "upimapi.py"
 - "xml2-config.bak"
 - "diamond"
 - "normalizer"
 - "tqdm"
 - "xslt-config"
 - "xsltproc"
 - "f2py3.10"
 - "2to3-3.10"
 - "idle3.10"
 - "pydoc3.10"
versions:
 - "1.8.5--hdfd78af_0"
 - "1.8.8--hdfd78af_0"
 - "1.8.10--hdfd78af_0"
 - "1.8.13--hdfd78af_0"
 - "1.8.14--hdfd78af_0"
 - "1.9.0--hdfd78af_0"
 - "1.10.0--hdfd78af_0"
 - "1.11.2--hdfd78af_0"
 - "1.12.0--hdfd78af_0"
 - "1.12.1--hdfd78af_0"
 - "1.12.2--hdfd78af_0"
 - "1.13.1--hdfd78af_0"
 - "1.12.3--hdfd78af_0"
description: "shpc-registry automated BioContainers addition for upimapi"
config: {"url": "https://biocontainers.pro/tools/upimapi", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for upimapi", "latest": {"1.13.1--hdfd78af_0": "sha256:9630a767b2809df2f9a9779c8610c5d87835940b2ca9abbc8580aeca3964a53d"}, "tags": {"1.8.5--hdfd78af_0": "sha256:3959e0b860808cf09b3ed70734918ddcba3747ccafb9a6b184e1f1d2cb56a2c7", "1.8.8--hdfd78af_0": "sha256:9799744544c1213f637e2463127f6acb0b6b85b6cc5780f5649faf3bddf496ee", "1.8.10--hdfd78af_0": "sha256:4b33202c951906af7f369471d216e4861830c9f2923bf5420a134af1df2dc7a7", "1.8.13--hdfd78af_0": "sha256:a891eb81eeff59c25543e567abe2d79d0f4b9709ae9fe36b486767b4ebed9f66", "1.8.14--hdfd78af_0": "sha256:7eb417266019cfcb1f5a3c107edd0419afc5db0bd90b55eb0d368111cbc347d2", "1.9.0--hdfd78af_0": "sha256:0f748b64de5c9eb9254e7ddb845bfe68533f06f1cd3c54a9db957b206051ad49", "1.10.0--hdfd78af_0": "sha256:6eb714c322379993dc026b60ddebb70cbcdcf96505b72a5b9795a212b5387b50", "1.11.2--hdfd78af_0": "sha256:1aa0e8e863fb7f76222818677e4bc226eb88ff8604d61c8394e332fd2168535c", "1.12.0--hdfd78af_0": "sha256:44722696a68af4a57d0d61572e5c7c6910d820b039946a8d428317a9eef780f8", "1.12.1--hdfd78af_0": "sha256:94ca10aeb9562e1f04c5e14fe8d6b9c07e246b08973329ac6f7ca8a1f69284a9", "1.12.2--hdfd78af_0": "sha256:fb2de2e6c6ca7b429ca9c12e907da98921af0c4e79b18851305aacae85c67a91", "1.13.1--hdfd78af_0": "sha256:9630a767b2809df2f9a9779c8610c5d87835940b2ca9abbc8580aeca3964a53d", "1.12.3--hdfd78af_0": "sha256:93edcc4b8e8075e975cb7e76db3d8f620480ddca561300d59254cfd7f997dabb"}, "docker": "quay.io/biocontainers/upimapi", "aliases": {"firefox": "/usr/local/bin/firefox", "geckodriver": "/usr/local/bin/geckodriver", "upimapi.py": "/usr/local/bin/upimapi.py", "xml2-config.bak": "/usr/local/bin/xml2-config.bak", "diamond": "/usr/local/bin/diamond", "normalizer": "/usr/local/bin/normalizer", "tqdm": "/usr/local/bin/tqdm", "xslt-config": "/usr/local/bin/xslt-config", "xsltproc": "/usr/local/bin/xsltproc", "f2py3.10": "/usr/local/bin/f2py3.10", "2to3-3.10": "/usr/local/bin/2to3-3.10", "idle3.10": "/usr/local/bin/idle3.10", "pydoc3.10": "/usr/local/bin/pydoc3.10"}}
---

This module is a singularity container wrapper for quay.io/biocontainers/upimapi.
shpc-registry automated BioContainers addition for upimapi
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/upimapi
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/upimapi:1.13.1--hdfd78af_0
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/upimapi/1.13.1--hdfd78af_0
$ module help quay.io/biocontainers/upimapi/1.13.1--hdfd78af_0
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### upimapi-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### upimapi-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### upimapi-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### upimapi-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### upimapi-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### upimapi-inspect-deffile:

```bash
$ singularity inspect -d <container>
```


#### firefox

```bash
$ singularity exec <container> /usr/local/bin/firefox
$ podman run --it --rm --entrypoint /usr/local/bin/firefox   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/firefox   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### geckodriver

```bash
$ singularity exec <container> /usr/local/bin/geckodriver
$ podman run --it --rm --entrypoint /usr/local/bin/geckodriver   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/geckodriver   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### upimapi.py

```bash
$ singularity exec <container> /usr/local/bin/upimapi.py
$ podman run --it --rm --entrypoint /usr/local/bin/upimapi.py   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/upimapi.py   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### xml2-config.bak

```bash
$ singularity exec <container> /usr/local/bin/xml2-config.bak
$ podman run --it --rm --entrypoint /usr/local/bin/xml2-config.bak   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/xml2-config.bak   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### diamond

```bash
$ singularity exec <container> /usr/local/bin/diamond
$ podman run --it --rm --entrypoint /usr/local/bin/diamond   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/diamond   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### normalizer

```bash
$ singularity exec <container> /usr/local/bin/normalizer
$ podman run --it --rm --entrypoint /usr/local/bin/normalizer   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/normalizer   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### tqdm

```bash
$ singularity exec <container> /usr/local/bin/tqdm
$ podman run --it --rm --entrypoint /usr/local/bin/tqdm   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/tqdm   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### xslt-config

```bash
$ singularity exec <container> /usr/local/bin/xslt-config
$ podman run --it --rm --entrypoint /usr/local/bin/xslt-config   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/xslt-config   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### xsltproc

```bash
$ singularity exec <container> /usr/local/bin/xsltproc
$ podman run --it --rm --entrypoint /usr/local/bin/xsltproc   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/xsltproc   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### f2py3.10

```bash
$ singularity exec <container> /usr/local/bin/f2py3.10
$ podman run --it --rm --entrypoint /usr/local/bin/f2py3.10   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/f2py3.10   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### 2to3-3.10

```bash
$ singularity exec <container> /usr/local/bin/2to3-3.10
$ podman run --it --rm --entrypoint /usr/local/bin/2to3-3.10   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/2to3-3.10   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### idle3.10

```bash
$ singularity exec <container> /usr/local/bin/idle3.10
$ podman run --it --rm --entrypoint /usr/local/bin/idle3.10   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/idle3.10   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### pydoc3.10

```bash
$ singularity exec <container> /usr/local/bin/pydoc3.10
$ podman run --it --rm --entrypoint /usr/local/bin/pydoc3.10   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/pydoc3.10   -v ${PWD} -w ${PWD} <container> -c " $@"
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
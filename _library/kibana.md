---
layout: container
name:  "kibana"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/kibana/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/kibana/container.yaml"
updated_at: "2023-04-02 03:35:17.648918"
latest: "8.6.2"
container_url: "https://hub.docker.com/_/kibana"
aliases:
 - "kibana"
 - "kibana-encryption-keys"
 - "kibana-keystore"
 - "kibana-plugin"
versions:
 - "7.12.0"
 - "7.12.1"
 - "7.13.1"
 - "7.13.2"
 - "7.13.3"
 - "7.14.0"
 - "7.14.2"
 - "7.16.2"
 - "7.16.3"
 - "8.0.0"
 - "8.1.2"
 - "8.0.1"
 - "7.17.2"
 - "8.1.3"
 - "7.17.3"
 - "8.2.2"
 - "7.17.4"
 - "8.2.3"
 - "8.4.0"
 - "8.3.3"
 - "8.4.1"
 - "8.4.2"
 - "8.5.1"
 - "8.4.3"
 - "8.5.3"
 - "8.6.0"
 - "8.6.2"
description: "Kibana gives shape to any kind of data — structured and unstructured — indexed in Elasticsearch."
config: {"docker": "kibana", "url": "https://hub.docker.com/_/kibana", "maintainer": "@vsoch", "description": "Kibana gives shape to any kind of data \u2014 structured and unstructured \u2014 indexed in Elasticsearch.", "latest": {"8.6.2": "sha256:a2867926b3fc1c72731c35b428aca04fa819e62e910e06896ad0472d35921380"}, "tags": {"7.12.0": "sha256:767581addfa1f3c0520774a30c5d872bbc8f833e172d93685baf89c579a1808a", "7.12.1": "sha256:e96f8b6a90db0b4ba804f7023922448a1d752a85e77f6c645ec309fa0328627d", "7.13.1": "sha256:298a8520298f229f4be784f8fb204976b4e5215b89968f82bc45a469c00933ab", "7.13.2": "sha256:3d975ad10f72f05e3b572302f5545206de7be1d3f1d7060ce42cc8d5fa8efc78", "7.13.3": "sha256:17e13d811898aac8bfe6f4bf58c287381aaafa1fef1435f60b56886a30ec4500", "7.14.0": "sha256:7188839aee88057c1f92aaff12d6ca4f54f5f89c1a07caedbc0247c4ec041392", "7.14.2": "sha256:d3eaf39c5aae353a9edae380030188ed712547a31954c8057d069ef8f2d8cbba", "7.16.2": "sha256:cbff0e7f8200798130dc9ebca666c89d440f203272d66b007763ef554b21d0f0", "7.16.3": "sha256:a9bb1d796ca13a9d658c7ca4e3ca78ec555e532256ee3246addcf7606cc55527", "8.0.0": "sha256:498cfc53922d8299baa88e5a0f306a7fbf7f50bd85ac79b4eb43cbfd2ed89ec9", "8.1.2": "sha256:16522ca04a01c252ff4785f0c8102178995d3bc31bb4302abc49903623fad3b6", "8.0.1": "sha256:1ec3a471e124c74a404c0d15820ff038d6e68241788bc6ff77b6462adedc654e", "7.17.2": "sha256:214302162d75a7c8ade156b3298f3e12ba275bc537503109f13a8caac33fbef0", "8.1.3": "sha256:54160acbcec72562994675bcc84ff5241c54d0ad1e89cc6c5c1236b15f210b8f", "7.17.3": "sha256:e2e2031c15be40af4369fe04db4d91d65976b39c06f70447d878a1d44b9915be", "8.2.2": "sha256:cf34801f36a2e79c834b3cdeb0a3463ff34b8d8588c3ccdd47212c4e0753f8a5", "7.17.4": "sha256:13572cada04ff3730aa7cb6ebc0e0f28e0ae7b4a3a4304fff5104e011b2cba05", "8.2.3": "sha256:d285696735a16772037f6ef7e763a9a347d2538c9ffd584f64c854b01a37f5d7", "8.4.0": "sha256:5c264dd22279f9285175f547d34d76ad7f370070d7ff2f3dffb000dd0f7cf5af", "8.3.3": "sha256:f62c3a08d9c9b9b8f1ac9ea02e370cf75094312cb6e51ffd83a9504174daa786", "8.4.1": "sha256:3f73f7b286c1821f4c238497ed972bbcc3d1b2796da8a660b15f8a891b7c2d29", "8.4.2": "sha256:8117be633ad6c81a49edbbf08ced1c816b06cbd3de6f37f4bfbc6a981b3b9271", "8.5.1": "sha256:09d6267c4d0433f5a52d3ade36a518adfaab0ef1b43951a0c064cb0e00b2c914", "8.4.3": "sha256:88b09cc593f6808cb9dfc8c3c13d94aa3c798b16f0a40d66247bd5be91a318d5", "8.5.3": "sha256:bb02932d930f2f23c9ef3047b990095b07b5e8b04c7f1831dd0c99cd199a57ec", "8.6.0": "sha256:71d8a59d32b181c3b3c04a4fecf2197f00eb381659510d04261c2cd5d43a0225", "8.6.2": "sha256:a2867926b3fc1c72731c35b428aca04fa819e62e910e06896ad0472d35921380"}, "aliases": {"kibana": "/usr/share/kibana/bin/kibana", "kibana-encryption-keys": "/usr/share/kibana/bin/kibana-encryption-keys", "kibana-keystore": "/usr/share/kibana/bin/kibana-keystore", "kibana-plugin": "/usr/share/kibana/bin/kibana-plugin"}}
---

This module is a singularity container wrapper for kibana.
Kibana gives shape to any kind of data — structured and unstructured — indexed in Elasticsearch.
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install kibana
```

Or a specific version:

```bash
$ shpc install kibana:8.6.2
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load kibana/8.6.2
$ module help kibana/8.6.2
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### kibana-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### kibana-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### kibana-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### kibana-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### kibana-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### kibana-inspect-deffile:

```bash
$ singularity inspect -d <container>
```


#### kibana

```bash
$ singularity exec <container> /usr/share/kibana/bin/kibana
$ podman run --it --rm --entrypoint /usr/share/kibana/bin/kibana   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/share/kibana/bin/kibana   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### kibana-encryption-keys

```bash
$ singularity exec <container> /usr/share/kibana/bin/kibana-encryption-keys
$ podman run --it --rm --entrypoint /usr/share/kibana/bin/kibana-encryption-keys   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/share/kibana/bin/kibana-encryption-keys   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### kibana-keystore

```bash
$ singularity exec <container> /usr/share/kibana/bin/kibana-keystore
$ podman run --it --rm --entrypoint /usr/share/kibana/bin/kibana-keystore   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/share/kibana/bin/kibana-keystore   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### kibana-plugin

```bash
$ singularity exec <container> /usr/share/kibana/bin/kibana-plugin
$ podman run --it --rm --entrypoint /usr/share/kibana/bin/kibana-plugin   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/share/kibana/bin/kibana-plugin   -v ${PWD} -w ${PWD} <container> -c " $@"
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
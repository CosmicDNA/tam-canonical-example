# Token Auth Middleware - Canonical Example

The purpose of this example is to prove the concept and auxiliate debugging why the Plover websocket plugin at https://github.com/CosmicDNA/plover_websocket_server/tree/benchmark-01 is failing to work as intended as opposed to this canonical implementation.

# Test Script

Before you continue, make sure you have `jq` installed in your terminal.
The test script that would evidence the problem or not is:

1. Run `./scripts/run.sh` in the terminal.
2. Run `./scripts/test.sh` in another terminal.

You should then see in the terminal:
```shell
{
  "status": "connected"
}
```

3. Follow the instructions at https://github.com/CosmicDNA/tam-canonical-example-test. You should then see in the browser:

![Status JSON data](/src/assets/Status.png)

From the outset, the successful completion of this test means that both middlewares are working as intended.
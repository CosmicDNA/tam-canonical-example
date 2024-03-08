# Token Auth Middleware - Canonical Example

The purpose of this example is to prove the concept and auxiliate debugging why the Plover websocket plugin at https://github.com/CosmicDNA/plover_websocket_server/tree/benchmark-01 is failing to work as intended as opposed to this canonical implementation.

# Test Script

Before you continue, make sure you have `jq` installed in your terminal.
The test script that would evidence the problem or not is:

1. Run `python3 -m venv .venv` to create a new virtual environment.
2. Activate env and run `pip install -r requirements.txt`
3. Run `./scripts/run.sh` in the terminal.
4. Run `./scripts/test.sh` in another terminal.

You should then see in the terminal:
```shell
{
  "status": "connected"
}
```

5. Follow the instructions at https://github.com/CosmicDNA/tam-canonical-example-test. You should then see in the browser:

![Status JSON data](/src/assets/Status.png)

From the outset, the successful completion of this test means that both middlewares are working as intended.

# Plover Plugin Test Script

1. Install Plover
2. Within Plover's installation directory, run the following to install the Plover Websocket Plugin:

```shell
.\plover_console -s plover_plugins install git+https://github.com/CosmicDNA/plover_websocket_server.git@benchmark-01
```

3. To configure the plugin, create a file named plover_engine_server_config.json inside Plover's configuration directory (same directory as plover.cfg file in windows that is C:\Users\your_user_name\AppData\Local\plover\plover).

4. Create file called `plover_engine_server_config.json` with the contents:

```json
{
  "host": "localhost",
  "port": 8086,
  "secretkey": "my-secret-token"
}
```

3. Open Plover.
4. Click on Configure Gear, select Plugins tab, make sure the websocket plugin is enabled there.

By the time you are reading this, the websocket server should have already started on port 8086.

5. You can now run https://github.com/CosmicDNA/tam-canonical-example-test again but before you do, make sure you have set the following line [App.jsx #L11](https://github.com/CosmicDNA/tam-canonical-example-test/blob/main/src/App.jsx#L11) to:

```jsx
const res = await fetch('http://localhost:8086/protocol', {
```

### Overview

This project explores modern, production‑ready communication standards using Python. Each example is minimal but complete, showcasing:

- REST (HTTP/1.1)
- Streamable HTTP (chunked & HTTP/2 server push)
- GraphQL
- gRPC & gRPC‑Web
- WebSockets
- Server‑Sent Events (SSE)
- Message Brokers (MQTT & AMQP)
- WebHooks
- HTTP/2 & HTTP/3 (QUIC)
- **WebTransport** (experimental bidirectional streaming over QUIC)

The goal is to compare architecture, data flow, latency, and developer experience.

---

### Communication Technologies

#### 1. **REST (HTTP/1.1)**
- Model: Request–Response, Stateless  
- Libraries: `FastAPI`, `Flask`, `Django`  
- Use Case: CRUD-driven APIs, widespread compatibility

#### 2. **Streamable HTTP** (chunked transfer / HTTP server-push)
- Model: Request–Response with streaming body  
- Use Case: Live logs, partial responses, long-running tasks  
- Libraries: `FastAPI` + `StreamingResponse`, `aiohttp`, `httpx`  
- Notes: HTTP/1.1 chunked is core; HTTP/2 multiplexing allows pushing responses by stream :contentReference[oaicite:1]{index=1}.

#### 3. **GraphQL**
- Model: Typed query language over HTTP or WebSocket  
- Libraries: `graphene`, `strawberry-graphql`, `ariadne`  
- Use Case: Flexible data-fetching APIs

#### 4. **gRPC**
- Model: Contract-first RPC over HTTP/2 (with Protobuf)  
- Libraries: `grpcio`, `grpcio-tools`, `protobuf`  
- Use Case: Microservices, high-performance APIs  
- Features: Supports unary and streaming RPCs, contract via `.proto` :contentReference[oaicite:2]{index=2}

#### 5. **gRPC‑Web**
- Model: Enables browser-compatible gRPC over HTTP/1 using a proxy (e.g., Envoy)  
- Libraries: Python demos like Sonora, `pyease-grpc` :contentReference[oaicite:3]{index=3}

#### 6. **WebSockets**
- Model: Full-duplex, bidirectional streams over TCP  
- Libraries: `websockets`, `FastAPI` + `starlette.websockets`, `Socket.IO`  
- Use Case: Chat, live games, interactive dashboards

#### 7. **Server‑Sent Events (SSE)**
- Model: One-way server → client stream via HTTP  
- Libraries: `sse-starlette`, `FastAPI` + `StreamingResponse`  
- Use Case: Live feeds, notifications

#### 8. **Message Brokers**
- MQTT (Pub/Sub): `paho-mqtt`
- AMQP (Queues): `aio_pika`, `kombu`  
- Use Case: IoT, decoupled distributed pipelines

#### 9. **WebHooks**
- Model: HTTP callbacks triggered by events  
- Libraries: Any HTTP server + `ngrok` or cloud function setup  
- Use Case: 3rd-party integrations (e.g., GitHub, Stripe)

#### 10. **HTTP/2 & HTTP/3 (QUIC)**
- HTTP/2: Multiplexing over TCP  
- HTTP/3: QUIC over UDP  
- Libraries: `httpx`, `hypercorn`, `aioquic`

#### 11. **WebTransport** (experimental)
- Model: Bidirectional, multiplexed streams over QUIC  
- Use Case: Low-latency file sync, game telemetry  
- Libraries: Experimental support via browser demos, Node.js  
- Note: Cutting-edge—worth a demo if you’re exploring HTTP/3 deeply

---

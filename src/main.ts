// -nocheck
// Fallback default apartment configuration in case fetching apartment.json fails (CORS block)
        const DEFAULT_CONFIG = {
            "rooms": [
                {"id": "utility_room", "coordinates": [80, 30], "outline": [76.05, 22.8, 7.9, 14.4]},
                {"id": "kitchen", "coordinates": [67, 30], "outline": [58.65, 22.45, 16.7, 15.1]},
                {"id": "dining_room", "coordinates": [51, 31], "outline": [43.3, 22.5, 15.2, 17.0]},
                {"id": "guest_bath", "coordinates": [39, 31], "outline": [34.7, 22.5, 8.6, 17.0]},
                {"id": "bedroom_3_front", "coordinates": [21, 34], "outline": [12.0, 22.5, 18.0, 23.0]},
                {"id": "master_bath", "coordinates": [67, 51], "outline": [59.8, 44.8, 14.4, 12.4]},
                {"id": "living_room", "coordinates": [50, 55], "outline": [41.25, 43.85, 17.5, 22.3]},
                {"id": "bedroom_2_middle", "coordinates": [32, 56], "outline": [23.5, 45.5, 17.0, 21.0]},
                {"id": "bedroom_1_master", "coordinates": [70, 68], "outline": [58.45, 57.45, 23.1, 21.1]},
                {"id": "entry", "coordinates": [79, 41], "outline": [75.9, 37.5, 6.0, 7.0]},
                {"id": "patio", "coordinates": [47, 72], "outline": [40.5, 66.5, 13.0, 11.0]},
                {"id": "patio_storage", "coordinates": [56, 72], "outline": [53.5, 66.5, 5.0, 11.0]},
                {"id": "bedroom_3_closet", "coordinates": [31, 27], "outline": [27.36, 22.25, 7.29, 9.5]},
                {"id": "bedroom_2_closet", "coordinates": [18, 51], "outline": [12.25, 45.5, 11.5, 11.0]},
                {"id": "master_closet", "coordinates": [78, 51], "outline": [74.0, 44.85, 8.0, 12.3]},
                {"id": "entry_closet", "coordinates": [74, 36], "outline": [71.9, 34.2, 4.2, 3.6]},
                {"id": "linen_closet", "coordinates": [33, 36], "outline": [30.9, 32.45, 4.2, 7.1]}
            ],
            "boxes": [
                {"type": "small", "dimensions_inches": [16, 12, 12], "max_weight_lbs": 30},
                {"type": "medium", "dimensions_inches": [18, 18, 16], "max_weight_lbs": 40},
                {"type": "large", "dimensions_inches": [24, 18, 18], "max_weight_lbs": 50},
                {"type": "wardrobe", "dimensions_inches": [24, 24, 40], "max_weight_lbs": 60}
            ],
            "inventory": [
                {"id": "microwave", "current_room": "kitchen", "dimensions_inches": [20, 15, 12], "fragile": false, "action": "store", "weight_lbs": 35.0},
                {"id": "stove", "current_room": "kitchen", "dimensions_inches": [30, 26, 36], "fragile": false, "action": "move", "weight_lbs": 150.0},
                {"id": "dish_rack", "current_room": "kitchen", "dimensions_inches": [15, 12, 10], "fragile": false, "action": "move", "weight_lbs": 5.0},
                {"id": "cookware", "current_room": "kitchen", "dimensions_inches": [18, 18, 16], "fragile": true, "action": "move", "weight_lbs": 25.0},
                {"id": "pantry_items", "current_room": "kitchen", "dimensions_inches": [12, 12, 12], "fragile": false, "action": "remove", "weight_lbs": 10.0},
                
                {"id": "couch", "current_room": "living_room", "dimensions_inches": [84, 36, 36], "fragile": false, "action": "remove", "weight_lbs": 120.0},
                {"id": "main_smart_tv_65", "current_room": "living_room", "dimensions_inches": [58, 4, 34], "fragile": true, "action": "move", "weight_lbs": 50.0},
                {"id": "second_smart_tv_55", "current_room": "living_room", "dimensions_inches": [49, 4, 29], "fragile": true, "action": "move", "weight_lbs": 40.0},
                {"id": "secondary_tv_stand", "current_room": "living_room", "dimensions_inches": [48, 18, 20], "fragile": false, "action": "remove", "weight_lbs": 60.0},
                {"id": "glass_computer_desk_lr", "current_room": "living_room", "dimensions_inches": [48, 24, 30], "fragile": true, "action": "remove", "weight_lbs": 50.0},
                {"id": "futon_couch", "current_room": "living_room", "dimensions_inches": [70, 36, 32], "fragile": false, "action": "move", "weight_lbs": 80.0},
                
                {"id": "mattress_queen", "current_room": "bedroom_1_master", "dimensions_inches": [60, 80, 10], "fragile": false, "action": "move", "weight_lbs": 80.0},
                {"id": "glass_computer_desk_master", "current_room": "bedroom_1_master", "dimensions_inches": [40, 24, 30], "fragile": true, "action": "remove", "weight_lbs": 40.0},
                {"id": "lg_monitor", "current_room": "bedroom_1_master", "dimensions_inches": [24, 8, 18], "fragile": true, "action": "move", "weight_lbs": 12.0},
                {"id": "desktop_heavy", "current_room": "bedroom_1_master", "dimensions_inches": [22, 10, 22], "fragile": true, "action": "move", "weight_lbs": 30.0},
                {"id": "desktop_medium", "current_room": "bedroom_1_master", "dimensions_inches": [18, 8, 18], "fragile": true, "action": "move", "weight_lbs": 20.0},
                {"id": "metal_bed_frame_queen", "current_room": "bedroom_1_master", "dimensions_inches": [60, 80, 8], "fragile": false, "action": "move", "weight_lbs": 40.0},

                {"id": "washer", "current_room": "utility_room", "dimensions_inches": [27, 30, 39], "fragile": false, "action": "move", "weight_lbs": 150.0},
                {"id": "dryer", "current_room": "utility_room", "dimensions_inches": [27, 30, 39], "fragile": false, "action": "move", "weight_lbs": 120.0},

                {"id": "full_mattress", "current_room": "bedroom_3_front", "dimensions_inches": [54, 75, 10], "fragile": false, "action": "move", "weight_lbs": 60.0},

                {"id": "twin_mattress", "current_room": "bedroom_2_middle", "dimensions_inches": [38, 75, 8], "fragile": false, "action": "move", "weight_lbs": 40.0},
                {"id": "twin_bed_frame", "current_room": "bedroom_2_middle", "dimensions_inches": [38, 75, 8], "fragile": false, "action": "move", "weight_lbs": 30.0},
                {"id": "bookshelf_3x3", "current_room": "bedroom_2_middle", "dimensions_inches": [36, 12, 36], "fragile": false, "action": "move", "weight_lbs": 30.0},

                {"id": "bathroom_items", "current_room": "master_bath", "dimensions_inches": [16, 12, 12], "fragile": true, "action": "move", "weight_lbs": 15.0},

                {"id": "deep_freeze", "current_room": "patio_storage", "dimensions_inches": [36, 24, 34], "fragile": false, "action": "remove", "weight_lbs": 100.0}
            ]
        };

        let currentData = JSON.parse(JSON.stringify(DEFAULT_CONFIG));
        
        // Simulation Output States
        let roomPackages = {};
        let usedBoxes = [];
        let unplacedItems = [];
        let tspPath = [];
        let tspDistance = 0;
        
        // Walkthrough State
        let currentStepIdx = 0;
        let walkTimer = null;
        
        // Editor zoom & pan states
        let zoomScale = 1.0;
        let panX = 0;
        let panY = 0;
        let isPanning = false;
        let panStartX = 0;
        let panStartY = 0;
        
        // Editor drag & select states
        let selectedRoomId = null;
        let dragMode = null; // 'move', 'resize-nw', 'resize-ne', 'resize-se', 'resize-sw'
        let dragStartMouseX = 0;
        let dragStartMouseY = 0;
        let dragStartOutline = null; // copy of [x, y, w, h]

        // Preload Floorplan Blueprint Image
        const floorplanImg = new Image();
        floorplanImg.src = "3x2_islandpark_14c1 2d- resied (square).webp";
        floorplanImg.onload = () => { if (typeof recalculate === 'function') recalculate(); };

        // UI Selectors
        const canvas = document.getElementById("floorplanCanvas");
        const ctx = canvas.getContext("2d");
        
        // Global scale functions mapping percentage coordinates (0-100) to client CSS pixels
        const scaleX = (val) => (val / 100) * canvas.clientWidth;
        const scaleY = (val) => (val / 100) * canvas.clientHeight;
        
        const configPanel = document.getElementById("configPanel");
        const configTextarea = document.getElementById("configTextarea");
        
        // Helper Math functions
        const volume = (dims) => dims[0] * dims[1] * dims[2];
        
        const getRotations = (dims) => {
            const rot = [
                [dims[0], dims[1], dims[2]],
                [dims[0], dims[2], dims[1]],
                [dims[1], dims[0], dims[2]],
                [dims[1], dims[2], dims[0]],
                [dims[2], dims[0], dims[1]],
                [dims[2], dims[1], dims[0]]
            ];
            return rot.filter((v, i, self) => self.findIndex(t => t.join(",") === v.join(",")) === i);
        };

        const calculateDistance = (p1, p2) => Math.sqrt((p1[0] - p2[0])**2 + (p1[1] - p2[1])**2);

        // --- 3D BIN PACKING FFD SOLVER (Javascript implementation) ---
        function runPackingSolver(data) {
            const rooms = data.rooms || [];
            const boxes = data.boxes || [];
            const inventory = data.inventory || [];
            
            // Filter items that we plan to move
            const moveInventory = inventory.filter(item => item.action === "move");
            
            // Map items to original room for final mapping
            const itemToRoom = {};
            inventory.forEach(item => { itemToRoom[item.id] = item.current_room; });
            
            // Sort items by volume decreasing (FFD)
            const sortedInventory = [...moveInventory].sort((a, b) => volume(b.dimensions_inches) - volume(a.dimensions_inches));
            
            const used_boxes = [];
            const unplaced_items = [];
            
            // Splitting free space using Guillotine split method
            function splitFreeSpace(freeSpace, itemDims) {
                const { x, y, z, dx, dy, dz } = freeSpace;
                const [w, d, h] = itemDims;
                const newSpaces = [];
                
                // Right space
                if (dx > w) {
                    newSpaces.push({ x: x + w, y, z, dx: dx - w, dy, dz });
                }
                // Front space
                if (dy > d) {
                    newSpaces.push({ x, y: y + d, z, dx: w, dy: dy - d, dz });
                }
                // Above space
                if (dz > h) {
                    newSpaces.push({ x, y, z: z + h, dx: w, dy: d, dz: dz - h });
                }
                return newSpaces;
            }
            
            for (const item of sortedInventory) {
                const item_id = item.id;
                const item_dims = item.dimensions_inches;
                const item_weight = item.weight_lbs || 5.0;
                const fragile = item.fragile || false;
                let placed = false;
                
                // Try existing boxes
                for (const box of used_boxes) {
                    const current_weight = box.items.reduce((sum, i) => sum + i.weight, 0);
                    if (current_weight + item_weight > box.max_weight) continue;
                    
                    for (let i = 0; i < box.free_spaces.length; i++) {
                        const freeSpace = box.free_spaces[i];
                        const rotations = getRotations(item_dims);
                        
                        for (const rot of rotations) {
                            const [w, d, h] = rot;
                            if (w <= freeSpace.dx && d <= freeSpace.dy && h <= freeSpace.dz) {
                                // Item fits!
                                box.items.push({
                                    id: item_id,
                                    position: [freeSpace.x, freeSpace.y, freeSpace.z],
                                    dimensions: rot,
                                    weight: item_weight,
                                    fragile
                                });
                                
                                const newSpaces = splitFreeSpace(freeSpace, rot);
                                box.free_spaces.splice(i, 1);
                                box.free_spaces.push(...newSpaces);
                                placed = true;
                                break;
                            }
                        }
                        if (placed) break;
                    }
                    if (placed) break;
                }
                
                // Open new box if not placed
                if (!placed) {
                    const sorted_box_types = [...boxes].sort((a, b) => volume(a.dimensions_inches) - volume(b.dimensions_inches));
                    for (const boxType of sorted_box_types) {
                        if (boxType.max_weight_lbs < item_weight) continue;
                        
                        const box_dims = boxType.dimensions_inches;
                        const rotations = getRotations(item_dims);
                        
                        for (const rot of rotations) {
                            const [w, d, h] = rot;
                            if (w <= box_dims[0] && d <= box_dims[1] && h <= box_dims[2]) {
                                const newBox = {
                                    type: boxType.type,
                                    dimensions: box_dims,
                                    max_weight: boxType.max_weight_lbs,
                                    free_spaces: [{ x: 0, y: 0, z: 0, dx: box_dims[0], dy: box_dims[1], dz: box_dims[2] }],
                                    items: []
                                };
                                
                                newBox.items.push({
                                    id: item_id,
                                    position: [0, 0, 0],
                                    dimensions: rot,
                                    weight: item_weight,
                                    fragile
                                });
                                
                                const initialSpace = newBox.free_spaces.pop();
                                const newSpaces = splitFreeSpace(initialSpace, rot);
                                newBox.free_spaces.push(...newSpaces);
                                
                                used_boxes.push(newBox);
                                placed = true;
                                break;
                            }
                        }
                        if (placed) break;
                    }
                }
                
                if (!placed) {
                    unplaced_items.push(item);
                }
            }
            
            // Map room items packing status
            const room_packages = {};
            rooms.forEach(r => { room_packages[r.id] = []; });
            
            used_boxes.forEach((box, index) => {
                box.items.forEach(item => {
                    const room = itemToRoom[item.id] || "unknown";
                    if (!room_packages[room]) room_packages[room] = [];
                    room_packages[room].push({
                        item_id: item.id,
                        box_type: box.type,
                        box_index: index + 1,
                        position: item.position,
                        dimensions: item.dimensions,
                        fragile: item.fragile
                    });
                });
            });
            
            return { room_packages, used_boxes, unplaced_items };
        }

        // --- TRAVELING SALESMAN PROBLEM (TSP) SOLVER ---
        function runTspSolver(data) {
            const rooms = data.rooms || [];
            const inventory = data.inventory || [];
            
            // Determine active rooms
            const activeRooms = new Set();
            inventory.forEach(item => {
                if (item.action === "move" || item.action === "remove") {
                    activeRooms.add(item.current_room);
                }
            });
            activeRooms.add("entry"); // starting loading zone
            
            const activeCoords = {};
            rooms.forEach(r => {
                if (activeRooms.has(r.id)) {
                    activeCoords[r.id] = r.coordinates;
                }
            });
            
            const roomIds = Object.keys(activeCoords);
            const otherRooms = roomIds.filter(id => id !== "entry");
            
            if (otherRooms.length === 0) {
                return { path: ["entry"], distance: 0.0 };
            }
            
            // Brute force permutations since N is small
            let bestDistance = Infinity;
            let bestPath = [];
            
            // Generate permutations helper
            function permute(arr) {
                let result = [];
                function helper(m, current) {
                    if (m.length === 0) {
                        result.push(current);
                    } else {
                        for (let i = 0; i < m.length; i++) {
                            let curr = m.slice();
                            let next = curr.splice(i, 1);
                            helper(curr.slice(), current.concat(next));
                        }
                    }
                }
                helper(arr, []);
                return result;
            }
            
            const perms = permute(otherRooms);
            const startCoords = activeCoords["entry"];
            
            for (const perm of perms) {
                let currentDist = 0.0;
                let prevCoords = startCoords;
                
                for (const roomId of perm) {
                    const currCoords = activeCoords[roomId];
                    currentDist += calculateDistance(prevCoords, currCoords);
                    prevCoords = currCoords;
                }
                
                currentDist += calculateDistance(prevCoords, startCoords);
                
                if (currentDist < bestDistance) {
                    bestDistance = currentDist;
                    bestPath = ["entry", ...perm, "entry"];
                }
            }
            
            return { path: bestPath, distance: bestDistance };
        }

        // --- DRAW AND VISUALIZE 2D CANVAS FLOOR PLAN ---
        function renderCanvas() {
            // Resize canvas to match container width
            const dpr = window.devicePixelRatio || 1;
            const rect = canvas.getBoundingClientRect();
            canvas.width = rect.width * dpr;
            canvas.height = rect.height * dpr;
            ctx.scale(dpr, dpr);
            
            const w = rect.width;
            const h = rect.height;
            
            ctx.save();
            ctx.translate(panX, panY);
            ctx.scale(zoomScale, zoomScale);
            
            // Draw floorplan blueprint image
            if (floorplanImg.complete && floorplanImg.naturalWidth !== 0) {
                ctx.drawImage(floorplanImg, 0, 0, w, h);
                // Draw a semi-transparent warm cream layer over the blueprint to make lines highly readable
                ctx.fillStyle = "rgba(250, 247, 242, 0.75)";
                ctx.fillRect(0, 0, w, h);
            } else {
                ctx.fillStyle = "#FAF7F2";
                ctx.fillRect(0, 0, w, h);
                
                // Draw grid overlay fallback
                ctx.strokeStyle = "rgba(26, 29, 32, 0.03)";
                ctx.lineWidth = 1;
                const gridSpacingX = w / 20;
                const gridSpacingY = h / 20;
                for (let i = 0; i <= w; i += gridSpacingX) {
                    ctx.beginPath();
                    ctx.moveTo(i, 0);
                    ctx.lineTo(i, h);
                    ctx.stroke();
                }
                for (let i = 0; i <= h; i += gridSpacingY) {
                    ctx.beginPath();
                    ctx.moveTo(0, i);
                    ctx.lineTo(w, i);
                    ctx.stroke();
                }
            }
            
            const rooms = currentData.rooms || [];
            
            // Draw connecting hallway visual lines
            ctx.strokeStyle = "rgba(26, 29, 32, 0.08)";
            ctx.lineWidth = 1.5;
            
            // Draw room shapes/cards
            rooms.forEach(room => {
                const [rx, ry] = room.coordinates;
                const cx = scaleX(rx);
                const cy = scaleY(ry);
                
                let px, py, pw, ph;
                if (room.outline) {
                    px = scaleX(room.outline[0]);
                    py = scaleY(room.outline[1]);
                    pw = scaleX(room.outline[2]);
                    ph = scaleY(room.outline[3]);
                } else {
                    px = cx - 35;
                    py = cy - 25;
                    pw = 70;
                    ph = 50;
                }
                
                const active = tspPath[currentStepIdx] === room.id;
                const isCloset = room.id.includes("closet");
                
                // Flat distinct color styling for different rooms
                if (active) {
                    ctx.shadowBlur = 0;
                    ctx.fillStyle = "rgba(200, 75, 49, 0.12)"; // light terracotta fill
                    ctx.strokeStyle = "#C84B31"; // terracotta red stroke
                    ctx.lineWidth = 2.5;
                } else if (isCloset) {
                    ctx.shadowBlur = 0;
                    ctx.fillStyle = "rgba(244, 63, 94, 0.12)"; // light rose fill
                    ctx.strokeStyle = "rgba(244, 63, 94, 0.75)"; // rose stroke
                    ctx.lineWidth = 1.5;
                    ctx.setLineDash([3, 3]);
                } else {
                    ctx.shadowBlur = 0;
                    ctx.fillStyle = "rgba(255, 255, 255, 0.75)"; // semi-transparent clean white card
                    ctx.strokeStyle = "rgba(26, 29, 32, 0.4)"; // clean charcoal border
                    ctx.lineWidth = 1.2;
                }
                
                // Draw rounded room card matching outline bounds
                drawRoundedRect(ctx, px, py, pw, ph, 4);
                ctx.fill();
                ctx.stroke();
                
                // Reset dash pattern and shadow
                ctx.setLineDash([]);
                ctx.shadowBlur = 0;
                
                // Draw room label in the center
                if (isCloset) {
                    ctx.fillStyle = "#e11d48";
                    ctx.font = "bold 8px Outfit";
                } else {
                    ctx.fillStyle = active ? "#C84B31" : "#1A1D20";
                    ctx.font = "bold 9px Outfit";
                }
                ctx.textAlign = "center";
                const label = room.id.toUpperCase().replace("_", " ");
                ctx.fillText(label, cx, cy - 4);
                
                // Draw room coordinate
                ctx.fillStyle = isCloset ? "rgba(225, 29, 72, 0.85)" : (active ? "rgba(200, 75, 49, 0.85)" : "rgba(26, 29, 32, 0.5)");
                ctx.font = "normal 7px JetBrains Mono";
                const sizeStr = room.outline ? ` (${parseFloat(room.outline[2]).toFixed(1)}x${parseFloat(room.outline[3]).toFixed(1)})` : "";
                ctx.fillText(`[${rx}, ${ry}]${sizeStr}`, cx, cy + 8);
                
                // Draw little box squares inside the room if items are packed here
                const itemsInRoom = (roomPackages[room.id] || []).filter(item => {
                    const original = currentData.inventory.find(i => i.id === item.item_id);
                    return original && original.action === "move";
                });
                const unboxedInRoom = currentData.inventory.filter(item => item.current_room === room.id && item.action === "move" && !roomPackages[room.id].some(p => p.item_id === item.id));
                
                let boxOffset = -((itemsInRoom.length + unboxedInRoom.length) * 9) / 2;
                itemsInRoom.slice(0, 5).forEach((packedItem, idx) => {
                    let boxColor = "#6E8B7E"; // small (sage green)
                    if (packedItem.box_type === "medium") boxColor = "#D2913C"; // mustard
                    if (packedItem.box_type === "large") boxColor = "#D3756B"; // light terracotta
                    if (packedItem.box_type === "wardrobe") boxColor = "#C84B31"; // terracotta
                    
                    ctx.fillStyle = boxColor;
                    ctx.fillRect(cx + boxOffset + (idx * 9), cy + 14, 7, 7);
                    ctx.strokeStyle = "rgba(26, 29, 32, 0.35)";
                    ctx.lineWidth = 0.5;
                    ctx.strokeRect(cx + boxOffset + (idx * 9), cy + 14, 7, 7);
                });
                
                unboxedInRoom.slice(0, 3).forEach((unboxed, idx) => {
                    ctx.fillStyle = "#7A5C61"; // unboxed/heavy (muted purple)
                    ctx.fillRect(cx + boxOffset + ((itemsInRoom.length + idx) * 9), cy + 14, 7, 7);
                    ctx.strokeStyle = "rgba(26, 29, 32, 0.35)";
                    ctx.lineWidth = 0.5;
                    ctx.strokeRect(cx + boxOffset + ((itemsInRoom.length + idx) * 9), cy + 14, 7, 7);
                });
            });
            
            // Draw routing optimal TSP lines (solid lines with mid-point arrows)
            if (tspPath.length > 1) {
                ctx.strokeStyle = "rgba(200, 75, 49, 0.75)"; // flat terracotta path
                ctx.lineWidth = 2.2;
                ctx.setLineDash([]);
                ctx.shadowBlur = 0;
                
                ctx.beginPath();
                for (let i = 0; i < tspPath.length; i++) {
                    const roomInfo = rooms.find(r => r.id === tspPath[i]);
                    if (roomInfo) {
                        const px = scaleX(roomInfo.coordinates[0]);
                        const py = scaleY(roomInfo.coordinates[1]);
                        if (i === 0) ctx.moveTo(px, py);
                        else ctx.lineTo(px, py);
                    }
                }
                ctx.stroke();
                
                // Draw route sequence indices and active step indicators
                for (let i = 0; i < tspPath.length - 1; i++) {
                    const startRoom = rooms.find(r => r.id === tspPath[i]);
                    const endRoom = rooms.find(r => r.id === tspPath[i+1]);
                    
                    if (startRoom && endRoom) {
                        const x1 = scaleX(startRoom.coordinates[0]);
                        const y1 = scaleY(startRoom.coordinates[1]);
                        const x2 = scaleX(endRoom.coordinates[0]);
                        const y2 = scaleY(endRoom.coordinates[1]);
                        
                        // Draw a subtle direction arrow at midpoint
                        const midX = (x1 + x2) / 2;
                        const midY = (y1 + y2) / 2;
                        const angle = Math.atan2(y2 - y1, x2 - x1);
                        
                        ctx.fillStyle = "rgba(200, 75, 49, 0.95)";
                        ctx.beginPath();
                        ctx.moveTo(midX, midY);
                        ctx.lineTo(midX - 7 * Math.cos(angle - Math.PI/6), midY - 7 * Math.sin(angle - Math.PI/6));
                        ctx.lineTo(midX - 7 * Math.cos(angle + Math.PI/6), midY - 7 * Math.sin(angle + Math.PI/6));
                        ctx.fill();
                    }
                }
            }
            
            // Draw current helper dot location
            const currentRoom = rooms.find(r => r.id === tspPath[currentStepIdx]);
            if (currentRoom) {
                const px = scaleX(currentRoom.coordinates[0]);
                const py = scaleY(currentRoom.coordinates[1]);
                
                // Draw flat blue helper cursor
                ctx.shadowBlur = 0;
                ctx.fillStyle = "#3b82f6";
                ctx.beginPath();
                ctx.arc(px, py - 20, 5.5, 0, 2 * Math.PI);
                ctx.fill();
                ctx.strokeStyle = "#FFFFFF";
                ctx.lineWidth = 1.5;
                ctx.stroke();
                ctx.strokeStyle = "rgba(26, 29, 32, 0.4)";
                ctx.lineWidth = 0.5;
                ctx.stroke();
            }
            
            // Draw selection borders & handles for selected room
            if (selectedRoomId) {
                const room = rooms.find(r => r.id === selectedRoomId);
                if (room && room.outline) {
                    const rx = scaleX(room.outline[0]);
                    const ry = scaleY(room.outline[1]);
                    const rw = scaleX(room.outline[2]);
                    const rh = scaleY(room.outline[3]);
                    
                    // Draw clean dashed charcoal border around the room
                    ctx.strokeStyle = "#1A1D20";
                    ctx.lineWidth = 1.5;
                    ctx.setLineDash([4, 4]);
                    ctx.strokeRect(rx - 2, ry - 2, rw + 4, rh + 4);
                    ctx.setLineDash([]);
                    
                    // Draw corner resize handles
                    const handleSize = 6;
                    ctx.fillStyle = "#ffffff";
                    ctx.strokeStyle = "#1A1D20";
                    ctx.lineWidth = 1;
                    
                    // NW
                    ctx.fillRect(rx - 3 - handleSize/2, ry - 3 - handleSize/2, handleSize, handleSize);
                    ctx.strokeRect(rx - 3 - handleSize/2, ry - 3 - handleSize/2, handleSize, handleSize);
                    // NE
                    ctx.fillRect(rx + rw + 3 - handleSize/2, ry - 3 - handleSize/2, handleSize, handleSize);
                    ctx.strokeRect(rx + rw + 3 - handleSize/2, ry - 3 - handleSize/2, handleSize, handleSize);
                    // SE
                    ctx.fillRect(rx + rw + 3 - handleSize/2, ry + rh + 3 - handleSize/2, handleSize, handleSize);
                    ctx.strokeRect(rx + rw + 3 - handleSize/2, ry + rh + 3 - handleSize/2, handleSize, handleSize);
                    // SW
                    ctx.fillRect(rx - 3 - handleSize/2, ry + rh + 3 - handleSize/2, handleSize, handleSize);
                    ctx.strokeRect(rx - 3 - handleSize/2, ry + rh + 3 - handleSize/2, handleSize, handleSize);
                }
            }
            
            ctx.restore();
        }
        
        function drawRoundedRect(ctx, x, y, width, height, radius) {
            ctx.beginPath();
            ctx.moveTo(x + radius, y);
            ctx.lineTo(x + width - radius, y);
            ctx.quadraticCurveTo(x + width, y, x + width, y + radius);
            ctx.lineTo(x + width, y + height - radius);
            ctx.quadraticCurveTo(x + width, y + height, x + width - radius, y + height);
            ctx.lineTo(x + radius, y + height);
            ctx.quadraticCurveTo(x, y + height, x, y + height - radius);
            ctx.lineTo(x, y + radius);
            ctx.quadraticCurveTo(x, y, x + radius, y);
            ctx.closePath();
        }

        // --- UPDATE SIDEBAR CHECKLIST FOR CURRENT ACTIVE ROOM ---
        function updateChecklist() {
            const activeRoomId = tspPath[currentStepIdx];
            if (!activeRoomId) return;
            
            const roomTitleEl = document.getElementById("currentRoomTitle");
            const roomCoordsEl = document.getElementById("currentRoomCoords");
            const itemsContainer = document.getElementById("roomChecklistItems");
            
            const roomData = currentData.rooms.find(r => r.id === activeRoomId);
            roomTitleEl.textContent = activeRoomId.toUpperCase().replace("_", " ");
            const sizeText = roomData.outline ? ` | Size: ${roomData.outline[2]}x${roomData.outline[3]}` : "";
            roomCoordsEl.textContent = `Coordinates: [${roomData.coordinates.join(", ")}]${sizeText}`;
            
            itemsContainer.innerHTML = "";
            
            if (activeRoomId === "entry" && currentStepIdx === 0) {
                itemsContainer.innerHTML = `
                    <div class="p-4 rounded border border-blue-200 bg-blue-50/50 text-xs text-blue-800">
                        <strong class="font-serif">[START CHECKLIST]</strong><br>
                        Walkthrough started. Prepare the entryway as the central staging and boxes loading zone next to the truck.
                    </div>`;
                return;
            }
            
            if (activeRoomId === "entry" && currentStepIdx === tspPath.length - 1) {
                itemsContainer.innerHTML = `
                    <div class="p-4 rounded border border-[#6E8B7E]/30 bg-[#6E8B7E]/5 text-xs text-[#4A5D54]">
                        <strong class="font-serif">[SIMULATION FINISHED]</strong><br>
                        Optimal route walkthrough completed successfully! Carry all remaining packed boxes and unboxed items out to the truck.
                    </div>`;
                return;
            }
            
            const items = currentData.inventory.filter(i => i.current_room === activeRoomId);
            
            if (items.length === 0) {
                itemsContainer.innerHTML = `<p class="text-xs text-gray-400 italic">No items to pack or process. Clean and inspect the walls/baseboards.</p>`;
                return;
            }
            
            // Build inventory checklist cards
            // Map packed items for quick reference
            const packedMap = {};
            if (roomPackages[activeRoomId]) {
                roomPackages[activeRoomId].forEach(p => {
                    packedMap[p.item_id] = p;
                });
            }
            
            items.forEach(item => {
                const action = item.action || "move";
                const isFragile = item.fragile || false;
                const fragileBadge = isFragile ? `<span class="px-1.5 py-0.5 rounded text-[8px] font-bold bg-[#C84B31]/10 text-[#C84B31] border border-[#C84B31]/20">FRAGILE</span>` : "";
                
                let actionBadge = "";
                let itemInstruction = "";
                let cardBorder = "border-gray-200 bg-white";
                
                if (action === "move") {
                    if (packedMap[item.id]) {
                        const p = packedMap[item.id];
                        actionBadge = `<span class="px-1.5 py-0.5 rounded text-[8px] font-bold bg-[#6E8B7E]/10 text-[#4A5D54] border border-[#6E8B7E]/20 font-mono">PACK</span>`;
                        itemInstruction = `
                            <div class="mt-2 text-xs text-gray-600 font-mono">
                                <strong>Box:</strong> ${p.box_type.toUpperCase()} Box #${p.box_index}<br>
                                <strong>Orientation:</strong> ${p.dimensions.join("x")} in<br>
                                <strong>Pos:</strong> ${p.position.join(", ")}
                            </div>`;
                        cardBorder = "border-[#6E8B7E]/30 bg-[#6E8B7E]/5";
                    } else {
                        actionBadge = `<span class="px-1.5 py-0.5 rounded text-[8px] font-bold bg-[#7A5C61]/10 text-[#5C4549] border border-[#7A5C61]/20 font-mono">MOVE UNBOXED</span>`;
                        itemInstruction = `
                            <div class="mt-1.5 text-xs text-[#5C4549]">
                                Wrap with blanket, carry directly to truck.
                            </div>`;
                        cardBorder = "border-[#7A5C61]/20 bg-[#7A5C61]/5";
                    }
                } else if (action === "remove") {
                    actionBadge = `<span class="px-1.5 py-0.5 rounded text-[8px] font-bold bg-[#C84B31]/10 text-[#A23B27] border border-[#C84B31]/20 font-mono">DISCARD</span>`;
                    itemInstruction = `<div class="mt-1.5 text-xs text-[#A23B27]">Carry to recycling bin or dumpster.</div>`;
                    cardBorder = "border-[#C84B31]/20 bg-[#C84B31]/5";
                } else if (action === "store") {
                    actionBadge = `<span class="px-1.5 py-0.5 rounded text-[8px] font-bold bg-gray-100 text-gray-600 border border-gray-200 font-mono">STAYS</span>`;
                    itemInstruction = `<div class="mt-1.5 text-xs text-gray-500">Stays with the apartment. Leave in place.</div>`;
                    cardBorder = "border-gray-200 bg-gray-50/50";
                }
                
                const itemCard = document.createElement("div");
                itemCard.className = `p-3 rounded border ${cardBorder} flex flex-col`;
                itemCard.innerHTML = `
                    <div class="flex justify-between items-start">
                        <div class="flex items-center space-x-2">
                            <input type="checkbox" class="w-4 h-4 bg-white border border-gray-300 rounded text-[#C84B31] focus:ring-0 focus:ring-offset-0">
                            <span class="font-semibold text-[#1A1D20] text-xs font-mono">${item.id}</span>
                        </div>
                        <div class="flex space-x-1">
                            ${fragileBadge}
                            ${actionBadge}
                        </div>
                    </div>
                    <div class="text-[10px] text-gray-500 mt-1 font-mono">Dims: ${item.dimensions_inches.join("x")} in | Wt: ${item.weight_lbs || 5.0} lbs</div>
                    ${itemInstruction}
                `;
                
                itemsContainer.appendChild(itemCard);
            });
        }

        // --- COMPILE DATA STATS SUMMARY PANEL ---
        function updateStats(stats) {
            const { used_boxes, unplaced_items, distance, path } = stats;
            
            document.getElementById("statDistance").textContent = `${distance.toFixed(1)} units`;
            document.getElementById("statRooms").textContent = `${path.length - 1} rooms`;
            document.getElementById("statBoxes").textContent = used_boxes.length;
            
            // Generate Box breakdown breakdown list
            const breakdownEl = document.getElementById("boxBreakdown");
            breakdownEl.innerHTML = "";
            
            const counts = {};
            used_boxes.forEach(box => {
                counts[box.type] = (counts[box.type] || 0) + 1;
            });
            
            const boxTypes = ["small", "medium", "large", "wardrobe"];
            boxTypes.forEach(type => {
                const count = counts[type] || 0;
                const breakdownCard = document.createElement("div");
                breakdownCard.className = "p-2 rounded bg-[#FAF7F2] border border-gray-200 flex justify-between";
                breakdownCard.innerHTML = `
                    <span class="capitalize text-gray-600 font-mono">${type}:</span>
                    <span class="font-bold text-[#1A1D20] font-mono">${count}</span>`;
                breakdownEl.appendChild(breakdownCard);
            });
            
            // Update indicator
            document.getElementById("currentStepIndicator").textContent = `Step ${currentStepIdx + 1} / ${tspPath.length}`;
        }

        // --- RE-EVALUATE PIPELINE (Packing & Walkthrough solver) ---
        function recalculate() {
            // Step 1: Pack items
            const packingResult = runPackingSolver(currentData);
            roomPackages = packingResult.room_packages;
            usedBoxes = packingResult.used_boxes;
            unplacedItems = packingResult.unplaced_items;
            
            // Step 2: TSP optimal walkthrough route
            const tspResult = runTspSolver(currentData);
            tspPath = tspResult.path;
            tspDistance = tspResult.distance;
            
            // Boundaries check
            if (currentStepIdx >= tspPath.length) {
                currentStepIdx = 0;
            }
            
            // Step 3: Draw floor plan on canvas & update checklists
            renderCanvas();
            updateChecklist();
            updateStats({
                used_boxes: usedBoxes,
                unplaced_items: unplacedItems,
                distance: tspDistance,
                path: tspPath
            });
        }

        // --- INITIALIZATION AND CORS FAILBACKS ---
        window.addEventListener("DOMContentLoaded", () => {
            // Attempt to load local apartment.json first (CORS may block this if opened directly as file URL)
            fetch("apartment.json")
                .then(res => {
                    if (!res.ok) throw new Error("Network response error loading JSON file.");
                    return res.json();
                })
                .then(data => {
                    console.log("Successfully loaded apartment.json");
                    currentData = data;
                    configTextarea.value = JSON.stringify(currentData, null, 2);
                    recalculate();
                })
                .catch(err => {
                    console.log("CORS block or missing apartment.json. Falling back to internal default config.");
                    configTextarea.value = JSON.stringify(currentData, null, 2);
                    recalculate();
                });
        });

        // Window resize handler for canvas
        window.addEventListener("resize", renderCanvas);

        // --- UI INTERACTIVE CONTROLS ---
        document.getElementById("prevStepBtn").addEventListener("click", () => {
            if (currentStepIdx > 0) {
                currentStepIdx--;
                renderCanvas();
                updateChecklist();
                document.getElementById("currentStepIndicator").textContent = `Step ${currentStepIdx + 1} / ${tspPath.length}`;
            }
        });

        document.getElementById("nextStepBtn").addEventListener("click", () => {
            if (currentStepIdx < tspPath.length - 1) {
                currentStepIdx++;
                renderCanvas();
                updateChecklist();
                document.getElementById("currentStepIndicator").textContent = `Step ${currentStepIdx + 1} / ${tspPath.length}`;
            }
        });

        // Config Drawer Toggle
        const toggleConfigBtn = document.getElementById("toggleConfigBtn");
        const closeConfigBtn = document.getElementById("closeConfigBtn");
        
        toggleConfigBtn.addEventListener("click", () => {
            configPanel.classList.remove("translate-x-full");
        });
        
        closeConfigBtn.addEventListener("click", () => {
            configPanel.classList.add("translate-x-full");
        });

        // Save Custom Config JSON input
        document.getElementById("saveConfigBtn").addEventListener("click", () => {
            try {
                const parsed = JSON.parse(configTextarea.value);
                currentData = parsed;
                recalculate();
                configPanel.classList.add("translate-x-full");
            } catch (err) {
                alert("Invalid JSON configuration. Please review syntax errors.");
            }
        });

        document.getElementById("resetConfigBtn").addEventListener("click", () => {
            if (confirm("Reset layout configuration back to defaults?")) {
                currentData = JSON.parse(JSON.stringify(DEFAULT_CONFIG));
                configTextarea.value = JSON.stringify(currentData, null, 2);
                recalculate();
            }
        });

        document.getElementById("recalculateBtn").addEventListener("click", () => {
            recalculate();
        });

        // Play Walking Tour Animation
        const playBtn = document.getElementById("playBtn");
        playBtn.addEventListener("click", () => {
            if (walkPlayInterval) {
                clearInterval(walkPlayInterval);
                walkPlayInterval = null;
                playBtn.textContent = "Play Tour";
                playBtn.className = "flex-1 py-2 bg-purple-600 hover:bg-purple-500 rounded-lg font-semibold text-sm";
            } else {
                playBtn.textContent = "Pause";
                playBtn.className = "flex-1 py-2 bg-yellow-600 hover:bg-yellow-500 rounded-lg font-semibold text-sm";
                walkPlayInterval = setInterval(() => {
                    if (currentStepIdx < tspPath.length - 1) {
                        currentStepIdx++;
                    } else {
                        currentStepIdx = 0;
                    }
                    renderCanvas();
                    updateChecklist();
                    document.getElementById("currentStepIndicator").textContent = `Step ${currentStepIdx + 1} / ${tspPath.length}`;
                }, 2500); // Step every 2.5 seconds
            }
        });

        document.getElementById("resetTourBtn").addEventListener("click", () => {
            if (walkPlayInterval) {
                clearInterval(walkPlayInterval);
                walkPlayInterval = null;
                playBtn.textContent = "Play Tour";
                playBtn.className = "flex-1 py-2 bg-purple-600 hover:bg-purple-500 rounded-lg font-semibold text-sm";
            }
            currentStepIdx = 0;
            renderCanvas();
            updateChecklist();
            document.getElementById("currentStepIndicator").textContent = `Step ${currentStepIdx + 1} / ${tspPath.length}`;
        });
        
        // --- EDITOR INTERACTIVE EVENT HANDLERS ---
        
        // Helper to convert screen coordinates to zoomed/panned workspace coordinates
        function getZoomedCoords(e) {
            const rect = canvas.getBoundingClientRect();
            const mx = e.clientX - rect.left;
            const my = e.clientY - rect.top;
            const zx = (mx - panX) / zoomScale;
            const zy = (my - panY) / zoomScale;
            return { mx, my, zx, zy, w: rect.width, h: rect.height };
        }
        
        // Helper to check if a point (mx, my) is over a room's corners
        function getHandleAt(mx, my) {
            if (!selectedRoomId) return null;
            const room = currentData.rooms.find(r => r.id === selectedRoomId);
            if (!room || !room.outline) return null;
            
            const rx = scaleX(room.outline[0]) * zoomScale + panX;
            const ry = scaleY(room.outline[1]) * zoomScale + panY;
            const rw = scaleX(room.outline[2]) * zoomScale;
            const rh = scaleY(room.outline[3]) * zoomScale;
            
            const handleSize = 10; // larger interactive target size for easier clicking
            
            // Check NW
            if (Math.abs(mx - (rx - 3)) < handleSize && Math.abs(my - (ry - 3)) < handleSize) return 'resize-nw';
            // Check NE
            if (Math.abs(mx - (rx + rw + 3)) < handleSize && Math.abs(my - (ry - 3)) < handleSize) return 'resize-ne';
            // Check SE
            if (Math.abs(mx - (rx + rw + 3)) < handleSize && Math.abs(my - (ry + rh + 3)) < handleSize) return 'resize-se';
            // Check SW
            if (Math.abs(mx - (rx - 3)) < handleSize && Math.abs(my - (ry + rh + 3)) < handleSize) return 'resize-sw';
            
            return null;
        }
        
        // Zoom buttons action
        document.getElementById("zoomInBtn").addEventListener("click", () => {
            const rect = canvas.getBoundingClientRect();
            const cx = rect.width / 2;
            const cy = rect.height / 2;
            
            // Current center point in workspace coords
            const wx = (cx - panX) / zoomScale;
            const wy = (cy - panY) / zoomScale;
            
            zoomScale = Math.min(5.0, zoomScale * 1.25);
            panX = cx - wx * zoomScale;
            panY = cy - wy * zoomScale;
            
            document.getElementById("zoomLabel").textContent = `${Math.round(zoomScale * 100)}%`;
            renderCanvas();
        });
        
        document.getElementById("zoomOutBtn").addEventListener("click", () => {
            const rect = canvas.getBoundingClientRect();
            const cx = rect.width / 2;
            const cy = rect.height / 2;
            
            const wx = (cx - panX) / zoomScale;
            const wy = (cy - panY) / zoomScale;
            
            zoomScale = Math.max(0.4, zoomScale / 1.25);
            panX = cx - wx * zoomScale;
            panY = cy - wy * zoomScale;
            
            document.getElementById("zoomLabel").textContent = `${Math.round(zoomScale * 100)}%`;
            renderCanvas();
        });
        
        document.getElementById("resetViewBtn").addEventListener("click", () => {
            zoomScale = 1.0;
            panX = 0;
            panY = 0;
            document.getElementById("zoomLabel").textContent = "100%";
            renderCanvas();
        });
        
        // Wheel zoom centered on cursor
        canvas.addEventListener("wheel", (e) => {
            e.preventDefault();
            const { mx, my, zx, zy } = getZoomedCoords(e);
            
            const zoomFactor = e.deltaY < 0 ? 1.1 : 0.9;
            zoomScale = Math.max(0.4, Math.min(5.0, zoomScale * zoomFactor));
            
            panX = mx - zx * zoomScale;
            panY = my - zy * zoomScale;
            
            document.getElementById("zoomLabel").textContent = `${Math.round(zoomScale * 100)}%`;
            renderCanvas();
        }, { passive: false });
        
        // Key state for Spacebar pan
        let spacePressed = false;
        window.addEventListener("keydown", (e) => {
            if (e.code === "Space" && document.activeElement !== configTextarea) {
                spacePressed = true;
                canvas.style.cursor = "grab";
            }
        });
        window.addEventListener("keyup", (e) => {
            if (e.code === "Space") {
                spacePressed = false;
                canvas.style.cursor = "default";
            }
        });
        
        // Mouse Down
        canvas.addEventListener("mousedown", (e) => {
            const { mx, my, zx, zy, w, h } = getZoomedCoords(e);
            const pctX = (zx / w) * 100;
            const pctY = (zy / h) * 100;
            
            // Space + Left Click or Middle Click = Pan
            if (spacePressed || e.button === 1 || e.button === 2) {
                isPanning = true;
                panStartX = mx - panX;
                panStartY = my - panY;
                canvas.style.cursor = "grabbing";
                e.preventDefault();
                return;
            }
            
            // Check if clicking a handle of selected room
            const handle = getHandleAt(mx, my);
            if (handle) {
                const room = currentData.rooms.find(r => r.id === selectedRoomId);
                dragMode = handle;
                dragStartMouseX = mx;
                dragStartMouseY = my;
                dragStartOutline = [...room.outline];
                e.preventDefault();
                return;
            }
            
            // Check if clicking inside any room outline
            let roomFound = null;
            const rooms = currentData.rooms || [];
            for (let i = rooms.length - 1; i >= 0; i--) {
                const room = rooms[i];
                if (room.outline) {
                    const rx1 = room.outline[0];
                    const ry1 = room.outline[1];
                    const rx2 = rx1 + room.outline[2];
                    const ry2 = ry1 + room.outline[3];
                    
                    if (pctX >= rx1 && pctX <= rx2 && pctY >= ry1 && pctY <= ry2) {
                        roomFound = room;
                        break;
                    }
                }
            }
            
            if (roomFound) {
                selectedRoomId = roomFound.id;
                dragMode = 'move';
                dragStartMouseX = mx;
                dragStartMouseY = my;
                dragStartOutline = [...roomFound.outline];
                canvas.style.cursor = "grabbing";
                renderCanvas();
            } else {
                // Clicked on empty space: select nothing, start panning if left click dragging
                selectedRoomId = null;
                isPanning = true;
                panStartX = mx - panX;
                panStartY = my - panY;
                canvas.style.cursor = "grabbing";
                renderCanvas();
            }
        });
        
        // Mouse Move
        canvas.addEventListener("mousemove", (e) => {
            const { mx, my, zx, zy, w, h } = getZoomedCoords(e);
            
            if (isPanning) {
                panX = mx - panStartX;
                panY = my - panStartY;
                renderCanvas();
                return;
            }
            
            if (dragMode && selectedRoomId) {
                const room = currentData.rooms.find(r => r.id === selectedRoomId);
                if (!room) return;
                
                const dx = (mx - dragStartMouseX) / zoomScale;
                const dy = (my - dragStartMouseY) / zoomScale;
                
                const dpctX = (dx / w) * 100;
                const dpctY = (dy / h) * 100;
                
                if (dragMode === 'move') {
                    room.outline[0] = parseFloat(Math.max(0, Math.min(100 - dragStartOutline[2], dragStartOutline[0] + dpctX)).toFixed(2));
                    room.outline[1] = parseFloat(Math.max(0, Math.min(100 - dragStartOutline[3], dragStartOutline[1] + dpctY)).toFixed(2));
                } else if (dragMode === 'resize-se') {
                    room.outline[2] = parseFloat(Math.max(1.0, Math.min(100 - dragStartOutline[0], dragStartOutline[2] + dpctX)).toFixed(2));
                    room.outline[3] = parseFloat(Math.max(1.0, Math.min(100 - dragStartOutline[1], dragStartOutline[3] + dpctY)).toFixed(2));
                } else if (dragMode === 'resize-sw') {
                    const newX = Math.max(0, Math.min(dragStartOutline[0] + dragStartOutline[2] - 1.0, dragStartOutline[0] + dpctX));
                    room.outline[2] = parseFloat((dragStartOutline[0] + dragStartOutline[2] - newX).toFixed(2));
                    room.outline[0] = parseFloat(newX.toFixed(2));
                    room.outline[3] = parseFloat(Math.max(1.0, Math.min(100 - dragStartOutline[1], dragStartOutline[3] + dpctY)).toFixed(2));
                } else if (dragMode === 'resize-ne') {
                    room.outline[2] = parseFloat(Math.max(1.0, Math.min(100 - dragStartOutline[0], dragStartOutline[2] + dpctX)).toFixed(2));
                    const newY = Math.max(0, Math.min(dragStartOutline[1] + dragStartOutline[3] - 1.0, dragStartOutline[1] + dpctY));
                    room.outline[3] = parseFloat((dragStartOutline[1] + dragStartOutline[3] - newY).toFixed(2));
                    room.outline[1] = parseFloat(newY.toFixed(2));
                } else if (dragMode === 'resize-nw') {
                    const newX = Math.max(0, Math.min(dragStartOutline[0] + dragStartOutline[2] - 1.0, dragStartOutline[0] + dpctX));
                    room.outline[2] = parseFloat((dragStartOutline[0] + dragStartOutline[2] - newX).toFixed(2));
                    room.outline[0] = parseFloat(newX.toFixed(2));
                    const newY = Math.max(0, Math.min(dragStartOutline[1] + dragStartOutline[3] - 1.0, dragStartOutline[1] + dpctY));
                    room.outline[3] = parseFloat((dragStartOutline[1] + dragStartOutline[3] - newY).toFixed(2));
                    room.outline[1] = parseFloat(newY.toFixed(2));
                }
                
                // Keep center coordinates (labeled node position) in sync in integer percentage
                room.coordinates[0] = Math.round(room.outline[0] + room.outline[2] / 2);
                room.coordinates[1] = Math.round(room.outline[1] + room.outline[3] / 2);
                
                renderCanvas();
                return;
            }
            
            // Hover cursor styling helper
            const handle = getHandleAt(mx, my);
            if (handle) {
                if (handle === 'resize-nw' || handle === 'resize-se') canvas.style.cursor = 'nwse-resize';
                else canvas.style.cursor = 'nesw-resize';
                return;
            }
            
            // Check if hover inside a room
            const pctX = (zx / w) * 100;
            const pctY = (zy / h) * 100;
            let overRoom = false;
            const rooms = currentData.rooms || [];
            for (let i = 0; i < rooms.length; i++) {
                const room = rooms[i];
                if (room.outline) {
                    const rx1 = room.outline[0];
                    const ry1 = room.outline[1];
                    const rx2 = rx1 + room.outline[2];
                    const ry2 = ry1 + room.outline[3];
                    if (pctX >= rx1 && pctX <= rx2 && pctY >= ry1 && pctY <= ry2) {
                        overRoom = true;
                        break;
                    }
                }
            }
            
            if (overRoom) {
                canvas.style.cursor = "move";
            } else {
                canvas.style.cursor = spacePressed ? "grab" : "default";
            }
        });
        
        // Mouse Up / Leave
        function stopDragging() {
            if (isPanning) {
                isPanning = false;
                canvas.style.cursor = spacePressed ? "grab" : "default";
            }
            if (dragMode) {
                dragMode = null;
                canvas.style.cursor = "default";
                configTextarea.value = JSON.stringify(currentData, null, 2);
                recalculate();
            }
        }
        canvas.addEventListener("mouseup", stopDragging);
        canvas.addEventListener("mouseleave", stopDragging);
    
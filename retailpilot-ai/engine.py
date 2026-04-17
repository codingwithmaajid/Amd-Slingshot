import json

class RetailDecisionEngine:
    def __init__(self, data_path='data/sample.json'):
        import os
        # Ensure we use an absolute path relative to the script
        base_dir = os.path.dirname(os.path.abspath(__file__))
        self.data_path = os.path.join(base_dir, data_path)
        self.load_data()

    def load_data(self):
        try:
            with open(self.data_path, 'r') as f:
                self.data = json.load(f)
        except FileNotFoundError:
            self.data = {"inventory": []}

    def process_request(self, prompt):
        prompt = prompt.lower().strip()
        inventory = self.data['inventory']
        
        # AGENT LOGIC: Find the best product match within the user prompt
        selected_item = None
        for item in inventory:
            name = item['name'].lower()
            sku = item['id'].lower()
            # Check for exact name or SKU match first
            if name in prompt or sku in prompt:
                selected_item = item
                break
            
            # Fallback: check if important keywords from the name are in the prompt
            # (e.g., "espresso" matches "Organic Espresso Beans")
            keywords = [w for w in name.split() if len(w) > 3]
            if any(k in prompt for k in keywords):
                selected_item = item
                break
        
        if not selected_item:
            return {
                "status": "unresolved",
                "action": "clarification_required",
                "message": "The system couldn't identify a specific product in your request."
            }

        # DECISION BRANCHING
        if selected_item['stock'] > 0:
            return {
                "status": "success",
                "decision": "EXECUTE_PURCHASE",
                "product": selected_item['name'],
                "action": "decrement_inventory_and_ship",
                "data": {
                    "sku": selected_item['id'],
                    "price": selected_item['price'],
                    "stock_left": selected_item['stock'] - 1
                }
            }
        else:
            # TRIGGER AUTONOMOUS RECOVERY
            sub_id = selected_item.get('substitute')
            sub_item = next((i for i in inventory if i['id'] == sub_id), None)
            
            return {
                "status": "out_of_stock",
                "decision": "AUTONOMOUS_RECOVERY",
                "action": "trigger_restock_and_substitute",
                "original_item": selected_item['name'],
                "suggested_substitute": sub_item['name'] if sub_item else "N/A",
                "message": f"Inventory for {selected_item['name']} is 0. System triggered supplier restock and routed to substitute."
            }